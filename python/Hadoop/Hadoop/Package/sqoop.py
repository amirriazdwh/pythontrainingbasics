'''
Module Name : sqoop.py
Created On : 10th Nov 2019
Created By : Amir Riaz
Purpose : This module caters with running sqoop related functionalities
'''

# Import Python Libraries
from pyodbc import connect
import sys
import os

# Import Package Modules
import configurations
import sessionutils


# Function to generate list databases command for connection validation
def gen_list_databases(connectionurl, username, password):
    try:
        sqpconnectlist = ['sqoop']
        sqpconnectlist.append('list-databases')
        sqpconnectlist.append('--connect')
        connurl = '"' + connectionurl + ';username=' + username + ';password=' + password + '"'
        sqpconnectlist.append(connurl)
        sqoopcmd = " ".join(sqpconnectlist)
        return sqoopcmd
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to generate the sqoop command for the run
def gen_sqoop_command(jrow, brow, metadbconn, jobrunid, sqplogpath):
    try:
        # Check if this is an incremental load
        # setenginecmd = 'set hive.execution.engine=mapreduce; '
        sqpexeccmd = None
        if jrow.incremental_key == None:
            sqpcmd = gen_import(jrow, brow, metadbconn, jobrunid, sqplogpath)
        else:
            incjobname = configurations.incjobnameprefix + jrow.src_schema + "_" + jrow.src_obj_name
            chkjobcmd = 'sqoop-job --show ' + incjobname
            try:
                os.system(jobchkstatus)
                jobexists = 'Y'
                sqpcmd = 'sqoop job --exec ' + incjobname
            except:
                jobexists = 'N'
            sqpcmd = gen_inc_import(jrow, brow, metadbconn, jobrunid, sqplogpath, jobexists, incjobname)
            sqpexeccmd = 'sqoop job --exec ' + incjobname
        return sqpcmd, sqpexeccmd
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to generate the full load (truncate load) import sqoop command
def gen_import(jrow, brow, metadbconn, jobrunid, sqplogpath):
    try:
        # Connection related arguments
        sqplist = ['sqoop']
        sqplist.append('import')

        sqplist.append('-D')
        mapmemoryconf = 'mapreduce.map.memory.mb=' + str(configurations.mappermemory)
        sqplist.append(mapmemoryconf)
        sqplist.append('-D')
        mapjavaconf = 'mapreduce.map.java.opts=' + configurations.javaheap
        sqplist.append(mapjavaconf)
        sqplist.append('-D')
        oraoopconf = 'oraoop.timestamp.string=' + configurations.oraooptimestamp
        sqplist.append(oraoopconf)
        sqplist.append('-D')
        mapubertaskconf = 'mapreduce.job.ubertask.enable=' + configurations.mapubertask
        sqplist.append(mapubertaskconf)

        if jrow.file_formats.upper() == 'AVRO':
            sqplist.append('-D')
            sqplist.append('mapreduce.job.user.classpath.first=true')

        sqplist.append('--connect')
        connurl = "'" + brow.sqp_conn_url + "'"
        sqplist.append(connurl)
        sqplist.append('--username')
        sqplist.append(brow.db_username)
        sqplist.append('--password')
        password = sessionutils.decryptpassword(brow.db_password)
        sqplist.append(password)
        if brow.sqp_driver != None:
            sqplist.append('--driver')
            sqplist.append(brow.sqp_driver)

        # import control arguments
        if jrow.query != None:
            if brow.db_type.upper() == 'SQL':
                jtimestampcmd = 'CURRENT_TIMESTAMP'
            elif brow.db_type.upper() == 'ORACLE':
                jtimestampcmd = 'SYSDATE'
            sqplist.append('--query')
            sqpquery = "'" + jrow.query.format(jtimestampcmd, configurations.hiveadditionalcolname) + "'"
            sqplist.append(sqpquery)
        else:
            sqplist.append('--table')
            tablename = jrow.src_schema + '.' + jrow.src_obj_name
            sqplist.append(tablename)
            if jrow.select_columns != None:
                sqplist.append('--columns')
                sqplist.append(jrow.select_columns)
            if jrow.where_clause != None:
                sqplist.append('--where')
                sqplist.append(jrow.where_clause)
        sqplist.append('--direct')
        sqplist.append('--fetch-size')
        sqplist.append(str(jrow.fetch_size))
        if jrow.split_by_key != None:
            sqplist.append('--split-by')
            sqplist.append(jrow.split_by_key)
            sqplist.append('-m')
            sqplist.append(str(jrow.mappers))
        else:
            sqplist.append('-m')
            sqplist.append('1')
        targetdir = getsqptargetdir(jrow)
        sqplist.append('--delete-target-dir')
        sqplist.append('--target-dir')
        sqplist.append(targetdir)
        if jrow.file_formats.upper() == 'PARQUET':
            sqplist.append('--as-parquetfile')
        elif jrow.file_formats.upper() == 'TEXT':
            sqplist.append('--as-textfile')
        elif jrow.file_formats.upper() == 'AVRO':
            sqplist.append('--as-avrodatafile')
        if jrow.compression_type != None:
            sqplist.append('--compress')
            sqplist.append('--compression-codec')
            sqplist.append(jrow.compression_type)

        # output formatting arguments
        if jrow.fields_terminated_by != None and jrow.file_formats.upper() == 'TEXT':
            sqplist.append('--fields-terminated-by')
            sqplist.append(jrow.fields_terminated_by)

        # code generation arguments
        clname = 'DL_INGESTION_' + str(brow.batch_id) + '_' + jrow.dest_schema + '_' + jrow.dest_obj_name
        sqplist.append('--class-name')
        sqplist.append(clname)
        sqplist.append('--null-string')
        sqplist.append("''")
        sqplist.append('--null-non-string')
        sqplist.append("''")
        outdir = getsqpoutdir(brow, jrow, jobrunid)
        sqplist.append('--outdir')
        sqplist.append(outdir)

        if jrow.java_mapping != None:
            javamapping = jrow.java_mapping + ',' + configurations.runtimecolmapping
        else:
            javamapping = configurations.runtimecolmapping

        sqplist.append('--map-column-java')
        sqplist.append(javamapping)

        # hive arguments
        if jrow.hive_mapping != None:
            hivemapping = jrow.hive_mapping + ',' + configurations.runtimecolmapping
        else:
            hivemapping = configurations.runtimecolmapping

        sqplist.append('--map-column-hive')
        sqplist.append(hivemapping)

        sqplist.append('--hive-import')
        sqplist.append('--hive-database')
        sqplist.append(jrow.dest_schema)
        sqplist.append('--hive-table')
        sqplist.append(jrow.dest_obj_name)
        sqplist.append('--hive-delims-replacement')
        sqplist.append("''")
        sqplist.append('--hive-overwrite')

        # Additional arguments which are not part of job config table and are required for specific use cases
        if jrow.additional_arguments == 1:
            conn = metadbconn
            cursor = conn.cursor()
            sqlquery = 'select * from {}.tbljobsqoopcmd where job_id = {} order by cmd_order'.format(
                configurations.metadb_schema, jrow.job_id)
            cursor.execute(sqlquery)
            for row in cursor:
                sqplist.append(row.job_command)
                sqplist.append(row.cmd_value)

        sqpcmd = "....".join(sqplist)

        return sqpcmd
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to generate the incremental import sqoop command
def gen_inc_import(jrow, brow, metadbconn, jobrunid, sqplogpath, jexistflag, jname):
    try:
        # sqoop job arguments
        sqplist = ['sqoop job']
        sqplist.append('-D')
        mapmemoryconf = 'mapreduce.map.memory.mb=' + str(configurations.mappermemory)
        sqplist.append(mapmemoryconf)
        sqplist.append('-D')
        mapjavaconf = 'mapreduce.map.java.opts=' + configurations.javaheap
        sqplist.append(mapjavaconf)
        sqplist.append('-D')
        oraoopconf = 'oraoop.timestamp.string=' + configurations.oraooptimestamp
        sqplist.append(oraoopconf)
        sqplist.append('-D')
        mapubertaskconf = 'mapreduce.job.ubertask.enable=' + configurations.mapubertask
        sqplist.append(mapubertaskconf)

        if jrow.file_formats.upper() == 'AVRO':
            sqplist.append('-D')
            sqplist.append('mapreduce.job.user.classpath.first=true')

        sqplist.append('--create')
        sqplist.append(jname)
        sqplist.append('-- import')

        # Connection related arguments
        sqplist.append('--connect')
        connurl = "'" + brow.sqp_conn_url + "'"
        sqplist.append(connurl)
        sqplist.append('--username')
        sqplist.append(brow.db_username)
        sqplist.append('--password')
        password = sessionutils.decryptpassword(brow.db_password)
        sqplist.append(password)
        if brow.sqp_driver != None:
            sqplist.append('--driver')
            sqplist.append(brow.sqp_driver)

        # import control arguments
        if jrow.query != None:
            if brow.db_type.upper() == 'SQL':
                jtimestampcmd = 'CURRENT_TIMESTAMP'
            elif brow.db_type.upper() == 'ORACLE':
                jtimestampcmd = 'SYSDATE'
            sqplist.append('--query')
            sqpquery = "'" + jrow.query.format(jtimestampcmd, configurations.hiveadditionalcolname) + "'"
            sqplist.append(sqpquery)
        else:
            sqplist.append('--table')
            tablename = jrow.src_schema + '.' + jrow.src_obj_name
            sqplist.append(tablename)
            if jrow.select_columns != None:
                sqplist.append('--columns')
                sqplist.append(jrow.select_columns)
            if jrow.where_clause != None:
                sqplist.append('--where')
                sqplist.append(jrow.where_clause)
        sqplist.append('--direct')
        sqplist.append('--fetch-size')
        sqplist.append(str(jrow.fetch_size))
        if jrow.split_by_key != None:
            sqplist.append('--split-by')
            sqplist.append(jrow.split_by_key)
            sqplist.append('-m')
            sqplist.append(str(jrow.mappers))
        else:
            sqplist.append('-m')
            sqplist.append('1')
        targetdir = getsqptargetdir(jrow)
        sqplist.append('--target-dir')
        sqplist.append(targetdir)
        if jrow.file_formats.upper() == 'PARQUET':
            sqplist.append('--as-parquetfile')
        elif jrow.file_formats.upper() == 'TEXT':
            sqplist.append('--as-textfile')
        elif jrow.file_formats.upper() == 'AVRO':
            sqplist.append('--as-avrodatafile')
        if jrow.compression_type != None:
            sqplist.append('--compress')
            sqplist.append('--compression-codec')
            sqplist.append(jrow.compression_type)

        # output formatting arguments
        if jrow.fields_terminated_by != None and jrow.file_formats.upper() == 'TEXT':
            sqplist.append('--fields-terminated-by')
            sqplist.append(jrow.fields_terminated_by)

        # code generation arguments
        clname = 'DL_INGESTION_' + str(brow.batch_id) + '_' + jrow.dest_schema + '_' + jrow.dest_obj_name
        sqplist.append('--class-name')
        sqplist.append(clname)
        sqplist.append('--null-string')
        sqplist.append("''")
        sqplist.append('--null-non-string')
        sqplist.append("''")
        outdir = getsqpoutdir(brow, jrow, jobrunid)
        sqplist.append('--outdir')
        sqplist.append(outdir)
        if jrow.java_mapping != None:
            sqplist.append('--map-column-java')
            sqplist.append(jrow.java_mapping)

        # hive arguments
        if jrow.hive_mapping != None:
            sqplist.append('--map-column-hive')
            sqplist.append(jrow.hive_mapping)
        sqplist.append('--hive-import')
        sqplist.append('--hive-database')
        sqplist.append(jrow.dest_schema)
        sqplist.append('--hive-table')
        sqplist.append(jrow.dest_obj_name)
        sqplist.append('--hive-delims-replacement')
        sqplist.append("''")

        # Incremental arguments
        sqplist.append('--incremental')
        sqplist.append('append')
        sqplist.append('--check-column')
        sqplist.append(jrow.incremental_key)

        # additional arguments which are not part of job config table and are required for specific use cases
        if jrow.additional_arguments == 1:
            conn = metadbconn
            cursor = conn.cursor()
            sqlquery = 'select * from {}.tbljobsqoopcmd where job_id = {} order by cmd_order'.format(
                configurations.metadb_schema, jrow.job_id)
            cursor.execute(sqlquery)
            for row in cursor:
                sqplist.append(row.job_command)
                sqplist.append(row.cmd_value)

        sqpcmd = " ".join(sqplist)
        return sqpcmd
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to get the records count affected by the sqoop job execution
def get_records_count(fpath):
    try:
        reccnt = 0
        reccntline = ''

        # Opening the sqoop log and reading the records count line
        # dummy line 19/11/29 14:52:39 INFO mapreduce.ImportJobBase: Retrieved 16 records.
        with open(fpath) as f:
            fread = f.readlines()
            for line in fread:
                if configurations.reccntfindString in line:
                    reccntline = line

        # Get the records count
        if reccntline != '':
            reclist = reccntline.split(' ')
            reccnt = int(reclist[-2])
        return reccnt
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to get the sqoop command out dir
def getsqpoutdir(brow, jrow, jobrunid):
    try:
        sqpoutdir = configurations.sqpoutdir + brow.batch_name.replace(' ',
                                                                       '') + "/" + jrow.dest_schema + "/" + jrow.dest_obj_name + "/" + str(
            jobrunid)
        currdatetime = sessionutils.getcurrdatetime()
        sqpoutdirfullpath = sqpoutdir + currdatetime
        return sqpoutdirfullpath
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to get the sqoop command target dir
def getsqptargetdir(jrow):
    try:
        if jrow.file_formats.upper() == 'PARQUET' or jrow.file_formats.upper() == 'TEXT':
            sqptargetdir = configurations.hdfstargetDir + jrow.dest_schema + ".db/" + jrow.dest_obj_name + "/"
        return sqptargetdir
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


def createavroexttable(jrow):
    try:
        extcommand = 'CREATE EXTERNAL TABLE ' + jrow.dest_schema + "." + jrow.dest_obj_name + \
                     'STORED AS AVRO' + \
                     'LOCATION' + "'" + avrodatalocation + "'" + \
                     'TBLPROPERTIES (' + "'" + 'avro.schema.url' + "'='" + avroschemalocation + "');"
        return extcommand
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to get the records count affected by the sqoop job execution
def chk_incr_zerorec(fpath):
    try:
        zerorecline = ''

        # Opening the sqoop log and reading the records count line
        # dummy line 19/11/29 14:52:39 INFO mapreduce.ImportJobBase: Retrieved 16 records.
        with open(fpath) as f:
            fread = f.readlines()
            for line in fread:
                if configurations.inczerorecString in line:
                    zerorecline = line

        # Get the records count
        if zerorecline != '':
            linefound = 1
        else:
            linefound = 0
        return linefound
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))
