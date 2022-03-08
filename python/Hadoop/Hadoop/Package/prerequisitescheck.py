'''
Module Name : prerequisites.py
Created On : 10th Nov 2019
Created By : Amir Riaz
Purpose : This module caters with checking all batch pre-resuites tests which helps in avoiding any unexpected errors 
          at the time of batch runs
'''

# Importing Python Libraries
from pyodbc import connect
from datetime import datetime as date
from getpass import getuser
import sys
import logging
import os
import calendar

# Importing Package Modules
import sessionutils
import sqoop
import configurations


# main function of the module
def prereqmain(batchid, metadbconn):
    try:
        dtrow = get_batch_details(batchid, metadbconn)
        check_batch_time(dtrow)
        check_batch_frequency(dtrow)
        check_batch_jobcount(dtrow)
        check_batch_type(dtrow)
        check_batchrun_user(dtrow)
        validate_source_connectivity(dtrow)
        return dtrow
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to get the batch details against a batch id
def get_batch_details(batchid, metadbconn):
    try:
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'select * from {}.tblbatchconfig a inner join {}.tblsourcedbconfig b on a.source_id = \
                     b.source_id and a.batch_id={}'.format(configurations.metadb_schema, configurations.metadb_schema,
                                                           batchid)
        cursor.execute(sqlquery)
        i = 0
        for row in cursor:
            datarow = row
            i = i + 1
        if i == 1:
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
            return datarow
        else:
            raise Exception('Unexpected number rows retrieved from metadata DB for requested batchid' + '\n'
                            + 'batchid : ' + str(batchid) + '\n'
                            + 'Rows Retrieved : ' + str(i) + '\n'
                            )
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to run the batch time check test
def check_batch_time(drow):
    try:
        batchstarttime = drow.batch_start_time
        batchendtime = drow.batch_end_time
        currentime = date.time(date.now()).replace(microsecond=0)
        if currentime >= batchstarttime and currentime <= batchendtime:
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
        else:
            raise Exception('Batch running outside specified run window' + '\n'
                            + 'Current Time : ' + str(currentime) + '\n'
                            + 'Batch Start Time : ' + str(batchstarttime) + '\n'
                            + 'Batch End Time : ' + str(batchendtime) + '\n'
                            )
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to run the batch frequency test
def check_batch_frequency(drow):
    try:
        if drow.batch_freq_logic == 'DAYS' and date.now().strftime("%a").upper() in drow.batch_freq_details.upper():
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
        elif drow.batch_freq_logic == 'DATES' and date.now().day in drow.batch_freq_details:
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
        elif drow.batch_freq_logic.upper() == 'CALCLOGIC' and drow.batch_freq_details.upper() == 'MONTHEND' and date.now().day == \
                calendar.monthrange(date.now().year, date.now().month)[1]:
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
        else:
            raise Exception('Run Frequency does not match with Batch frequency' + '\n'
                            + 'Current Day / Date : ' + str(date.now().strftime("%a")) + '/' + str(
                date.now().day) + '\n'
                            + 'Allowed Days / Date : ' + str(drow.batch_freq_details) + '\n'
                            )
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to run the valid job count test
def check_batch_jobcount(drow):
    try:
        if drow.batch_job_count > 0:
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
        else:
            raise Exception('Batch does not have any jobs available' + '\n'
                            + 'Tables Count Retrieved : ' + str(drow.batch_job_count) + '\n'
                            )
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to run the valid batch type test
def check_batch_type(drow):
    try:
        if drow.batch_type.upper() == "INGESTION":
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
        else:
            raise Exception('Batch Type value not correct' + '\n'
                            + 'Type Retrieved is : ' + str(drow.batch_type) + '\n'
                            )
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to run the valid batch run user test
def check_batchrun_user(drow):
    try:
        if drow.batch_linux_username.upper() == getuser().upper():
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
        else:
            raise Exception('Batch run user does not match with the specified user' + '\n'
                            + 'Batch run user : ' + str(getuser().upper()) + '\n'
                            + 'Retrieved user : ' + str(drow.batch_linux_username.upper()) + '\n'
                            )
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to validate the connectivity to batch source database
def validate_source_connectivity(drow):
    try:
        password = sessionutils.decryptpassword(drow.db_password)
        scmd = sqoop.gen_list_databases(drow.sqp_conn_url, drow.db_username, password)
        logging.info('Generated sqoop command is %s', scmd)
        sout, serr, returncode = sessionutils.rununixcommand(scmd, '')
        if returncode != 0:
            raise Exception(serr)
        else:
            logging.info('Sqoop command result is %s', sout)
            logging.info(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : ' + 'check completed')
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))
