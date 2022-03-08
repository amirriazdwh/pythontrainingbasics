from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pyodbc
import sys
import os
from config import gsproperty as conf
import mail
import subprocess
import re

def get_job_run_detail(cursor,job_id):
    job_last_run_date = cursor.execute("select job_id, last_run_date, status_time_count from (select job_id,"
                                       " cast(run_starttime as date) as last_run_date, CONCAT(run_status,'-',"
                                       "total_time_in_sec,'-',row_count) as status_time_count,row_number() over(partition by job_id"
                                       " order by run_starttime desc) as rnk from DLINGESTIONUAT.tbljobrundetails where job_id in ({0})) A"
                                       " where rnk = 1".format(job_id)).fetchall()
    return job_last_run_date

def get_prev_out(cursor,query_no):
    prev_out = cursor.execute(
        "select output from (select *, row_number() over(partition by Query_No order by Execution_date desc) as rnk"
        " from {}) a where rnk = 1 and query_no = {} ".format(
            conf.sql_result_table, query_no))

    result  = prev_out.fetchone()
    return int(result[0]) if result else result

def get_curr_count(spark,query):
    res = spark.sql(query)
    return int(re.sub('[^a-zA-Z0-9 \n\.]','',"{}".format(res.collect()[0][0]))) if bool(res.head(1)) else 0

def get_last_month_data(cursor):
    data = cursor.execute("select * from (select *, row_number() over(partition by Query_No order by Execution_date desc) "
                          "as rnk from {} where month(Execution_date) = month(dateadd(m,-1, getdate()))) a where rnk = 1".format(conf.sql_result_table)).fetchall()

    return data

def get_last_day_data(cursor):
    prev_out = cursor.execute("select Query_No,Output from (select *, row_number() over(partition by Query_No order by Execution_date desc) as rnk from {} where cast(Execution_date as date) = cast(dateadd(d,-1,getdate()) as date)) a where rnk = 1 ".format(conf.sql_result_table)).fetchall()

    return prev_out

def insert_result(cursor,query_no,curr_cnt,variance,exec_dt,status,table_name):

    #result = 'PASS' if variance < variance_limit else 'FAIL'
    query = "insert into {0}(Query_No,Execution_date,Output,Variance_Per,status_time_count,table_name) values(?,?,?,?,?,?)".format(conf.sql_result_table)
    cursor.execute(query,(query_no,exec_dt,curr_cnt,variance,status,table_name))
    cursor.commit()

def execute_queries(table_names, frequency):

    spark = SparkSession.builder.appName("QueryExecutor").enableHiveSupport().getOrCreate()
    identifiers = ",".join(map(lambda x:"'{0}'".format(x), table_names))
    freq_filter = ",".join(map(lambda x:"'{0}'".format(x), frequency))
    identifiers = "select distinct identifier from {}".format(conf.sql_config_table) if identifiers.upper() == "'ALL'" else identifiers
    freq_filter = "select distinct frequency from {}".format(conf.sql_config_table) if freq_filter.upper() == "'ALL'" else freq_filter
    properties = {"user": conf.sql_user, "password": conf.sql_password, "driver": conf.sql_driver}

    connection = pyodbc.connect(
        'DRIVER=' + conf.driver + ';SERVER=' + conf.server + ';DATABASE=' + conf.database + ';UID=' + conf.sql_user + ';PWD=' + conf.sql_password)

    cursor = connection.cursor()

    test_query = "SELECT * from {0} where identifier in ({1}) and frequency in ({2})".format(conf.sql_config_table, identifiers, freq_filter)

    print(test_query)

    cursor.execute("SELECT * from {0} where identifier in ({1}) and frequency in ({2})".format(conf.sql_config_table, identifiers, freq_filter))

    rows = cursor.fetchall()
    row_list = list(rows)
    job_id_list = ",".join(map(lambda x: "{}".format(int(getattr(x,'Job_id'))),filter(lambda x: getattr(x,'Job_id') != None, row_list)))
    print("job_id_list --> {}".format(job_id_list))
    job_run_details = get_job_run_detail(cursor,job_id_list) if job_id_list else []
    print("job_run_details --> {}".format(job_run_details))
    last_month_data = get_last_month_data(cursor)
    print("last_month_data --> {}".format(last_month_data))
    last_day_data = get_last_day_data(cursor)
    print("last_day_data --> {}".format(last_day_data))
    sr_no = 0
    exec_dt = datetime.now()
    print("exec_dt --> {}".format(exec_dt))
    data_to_write = spark.sql("select cast(null as int) as Sr_No, cast(null as int) as Query_No, cast(null as String) as Table_Name, cast(null as String) as Query, cast(null as string) as Description, cast(null as int) as Expected_Result, cast(null as int) as Output, cast(null as date) as Table_Last_Refresh_Date, cast(null as string) as Table_Refresh_Frequency, cast(null as float) as Variance_As_Of_Last_Execution, cast(null as float) as Variance_As_Of_Last_Month, cast(null as timestamp) as Execution_Date_Time")
    f_count=0

    if not rows:
        print("Provided Identifiers does not exist")
    else:
        for row in rows:
            try:
               query = getattr(row,'Query').replace('\n', ' ')
               query_no = getattr(row,'Query_No')
               job_id = getattr(row,'Job_id')
               #variance_limit = getattr(row,'Variance_Per')
               desc = getattr(row,'Description')
               Expected_Count = getattr(row,'Expected_Count')
               freq = getattr(row,'Frequency')
               last_day_filter = list(filter(lambda x: getattr(x, 'Query_No') == query_no, last_day_data))
               last_month_filter = list(filter(lambda x: getattr(x, 'Query_No') == query_no, last_month_data))
               tbl_details = list(filter(lambda x: getattr(x,'job_id') == job_id,job_run_details)) if job_id else None
               tbl_last_run_date = getattr(tbl_details[0], 'last_run_date') if tbl_details else None
               tbl_status = getattr(tbl_details[0], 'status_time_count') if tbl_details else None
               print("last_day_filter = {}".format(last_day_filter))
               print("last_month_filter = {}".format(last_month_filter))
               print("query_no = {}".format(query_no))
               print("tbl_details = {}".format(tbl_details))
               print("tbl_last_run_date = {}".format(tbl_last_run_date))
               print("tbl_status = {}".format(tbl_status))
               prev_cnt = int(getattr(last_day_filter[0], 'Output')) if last_day_filter else None
               last_month_cnt = int(getattr(last_month_filter[0], 'Output')) if last_month_filter else None
               sr_no+=1
               print("prev cnt = {}".format(prev_cnt))
               curnt_cnt = get_curr_count(spark,query)
               print("curr cnt = {}".format(curnt_cnt))
               print(query)
               variance = 0.0 if not prev_cnt or not curnt_cnt else float(curnt_cnt - prev_cnt) / prev_cnt
               last_month_variance = 0.0 if not last_month_cnt or not curnt_cnt else float(curnt_cnt - last_month_cnt) / last_month_cnt
               #temp_sub = query[query.rfind('from')+5::]
               #query_sub = temp_sub[:temp_sub.find(' ')+1] if temp_sub.find(' ') != -1 else temp_sub
               query_re_split = re.findall('\w+\.+\w+',query)
               #query_sub_split = query_sub.split('.')
               query_sub_split = query_re_split[0].split('.') if query_re_split else ['curation', 'dummy']
               db = query_sub_split[0].strip().lower()
               table_name = query_sub_split[1].strip().lower()
               print("variance = {}".format(variance))
               print("last_month_variance = {}".format(last_month_variance))
               print("db = {}".format(db))
               print("table_name = {}".format(table_name))
               # shell_cmd = "hadoop fs -ls -t -r /apps/hive/warehouse/{0}.db/{1}".format(db,table_name)
               shell_cmd = "hadoop fs -ls -t -r /warehouse/tablespace/external/hive/{0}.db/{1}".format(db,table_name)
               shell_cmd = shell_cmd + " | awk -F ' ' '{print $6}' | tail -n 1"
               print("shell_cmd = {}".format(shell_cmd)) 
               tab_last_ref = subprocess.check_output(shell_cmd, shell=True).decode('utf-8').strip()
               print("tab_last_ref = {}".format(tab_last_ref))
               tab_last_ref = tbl_last_run_date if not tab_last_ref or (tbl_last_run_date and datetime.strptime(str(tbl_last_run_date),'%Y-%m-%d') > datetime.strptime(tab_last_ref, '%Y-%m-%d')) else tab_last_ref
               print("tab_last_ref = {}".format(tab_last_ref))
			   
               data_to_write = data_to_write.unionAll(spark.sql("""select cast({0} as int) as Sr_No, cast({1} as int) as Query_No, cast('{2}' as String) as Table_Name, cast("{11}" as string) as Query, cast("{3}" as string) as Description, cast({4} as int) as Expected_Result, cast({7} as int) as Output, cast('{5}' as date) as Table_Last_Refresh_Date, cast('{6}' as string) as Table_Refresh_Frequency, cast({8} as float) as Variance_As_Of_Last_Execution, cast({9} as float) as Variance_As_Of_Last_Month, cast('{10}' as timestamp) as Execution_Date_Time""".format(sr_no,query_no,query_re_split[0],desc,Expected_Count,tab_last_ref,freq,curnt_cnt,format(variance*100,'.3f'),format(last_month_variance*100,'.3f'),exec_dt,query))) 

               insert_result(cursor,query_no,curnt_cnt,variance*100,exec_dt,tbl_status,query_re_split[0])
               if Expected_Count==0 and curnt_cnt!=0 or Expected_Count==1 and curnt_cnt==0:
                  f_count=f_count+1
            except:
               mail.send_mail('')
               pass
        connection.close()
        data_to_write = data_to_write.dropna('all')
        data_to_write.createOrReplaceTempView('qc_results')
        final_data_to_write = spark.sql('''select *, CASE
							WHEN Expected_Result = 0 AND Output = 0 THEN 'PASS'
							WHEN Expected_Result = 1 AND Output != 0 THEN 'PASS'
							ELSE 'FAIL'
						END AS Test_Result from qc_results''')
        #final_data_to_write.show()
        final_data_to_write.dropna('all').coalesce(1).write.mode('overwrite').csv("/warehouse/tablespace/external/hive/obtf_qc_output",header='true')
        subprocess.call('rm /home/cibg_uat_user/obtf/qc_framework/output/executor_result_{}.csv'.format(datetime.now().strftime('%Y%m%d')), shell=True)
        subprocess.call('hadoop fs -copyToLocal /warehouse/tablespace/external/hive/obtf_qc_output/*.csv /home/cibg_uat_user/obtf/qc_framework/output/executor_result_{}.csv'.format(datetime.now().strftime('%Y%m%d')), shell=True )
        if f_count!=0:
           mail.send_Failuremail('/home/cibg_uat_user/obtf/qc_framework/output/executor_result_{}.csv'.format(datetime.now().strftime('%Y%m%d')))
        else:
           mail.send_mail('/home/cibg_uat_user/obtf/qc_framework/output/executor_result_{}.csv'.format(datetime.now().strftime('%Y%m%d')))




if __name__ == "__main__":
    try:
        table_names = ['all'] if len(sys.argv) < 3 else sys.argv[2].split(",")
        frequency = ['all'] if len(sys.argv) < 2 else sys.argv[1].split(",")
        execute_queries(table_names, frequency)
    except Exception as e:
        print(e)
        mail.send_mail('')
