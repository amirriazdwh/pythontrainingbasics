'''
Module Name : batchdataderiv.py
Created On : 10th Nov 2019
Created By : Amir Riaz
Purpose : This module caters with deriving the run category based on logical interpretation
'''

# Importing Python Libraries
from pyodbc import connect
from datetime import datetime as date
import logging
import sys

# Importing Package Modules
import configurations


# Function to run the valid batch status test
def derive_runcategory(batchid, metadbconn):
    try:
        lastrunrowdet = ''
        crow = ''
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'select batch_run_id, \
                                run_status as prevrunstatus, \
                                cast(GETDATE() as date) as currdate, \
                                cast(run_starttime as date) as prevrundate,\
                                cast(getdate() as time) as currtime, \
                                batch_start_time as batchstarttime, \
                                batch_freq as frequency \
                                from ( \
                                select batch_id, batch_run_id, run_status, run_starttime, DENSE_RANK() OVER (order by run_endtime desc) rnk \
                                from {}.tblbatchrundetails where batch_id ={}) a, {}.tblbatchconfig b \
                                where a.batch_id = b.batch_id and a.rnk = 1'.format(configurations.metadb_schema,
                                                                                    batchid,
                                                                                    configurations.metadb_schema)
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        for lastrunrowdet in cursor:
            crow = lastrunrowdet
        logging.info('Last Run Status record found with details : %s', lastrunrowdet)

        # If batch frequency is daily
        if crow == '':
            category = 'LOAD'
        elif crow.frequency.upper() == 'DAILY':
            if crow.prevrunstatus.upper() == configurations.successstatus:
                category = 'LOAD'
            elif crow.prevrunstatus.upper() == configurations.failstatus:
                if crow.currdate > crow.prevrundate and crow.currtime >= crow.batchstarttime:
                    category = 'LOAD'
                else:
                    category = 'RERUN'
        elif crow.frequency.upper() == 'MONTHLY':
            if crow.prevrunstatus.upper() == configurations.successstatus:
                category = 'LOAD'
            elif crow.prevrunstatus.upper() == configurations.failstatus:
                if crow.currdate > crow.prevrundate and crow.currtime >= crow.batchstarttime:
                    category = 'LOAD'
                else:
                    category = 'RERUN'
        elif crow.frequency.upper() == 'INTRADAY':
            if crow.prevrunstatus.upper() == configurations.successstatus:
                category = 'LOAD'
            elif crow.prevrunstatus.upper() == configurations.failstatus:
                if crow.currrtime >= crow.batchstarttime:
                    category = 'LOAD'
                else:
                    category = 'RERUN'
        return category
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to check last batch status
def check_lastrun_status(batchid, metadbconn):
    try:
        prevbatchrunid = 0
        prevrunstatus = ''
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'select a.* from ( \
                        select batch_id, batch_run_id, run_status, DENSE_RANK() OVER (order by run_endtime desc) rnk \
                        from {}.tblbatchrundetails where batch_id = {}) a \
                        where rnk = 1'.format(configurations.metadb_schema, batchid)
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        for row in cursor:
            prevbatchrunid = row.batch_run_id
            prevrunstatus = row.run_status
            if prevrunstatus == configurations.runningstatus:
                raise Exception('Batch is already running' + '\n'
                                + 'Batch Run ID Record : ' + str(prevbatchrunid) + '\n'
                                )
        return prevbatchrunid, prevrunstatus
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))
