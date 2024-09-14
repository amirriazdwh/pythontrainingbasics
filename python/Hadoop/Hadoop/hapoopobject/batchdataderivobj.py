"""
created by :  Amir Riaz
"""
import logging
import sys
from pyodbc import connect
from datetime import datetime as date
import configurations

class BatchProcessor:
    def __init__(self, metadbconn):
        """
        Initialize with the metadata database connection.
        
        :param metadbconn: Database connection object.
        """
        self.conn = metadbconn
    
    def derive_runcategory(self, batchid):
        """
        Derives the run category for the given batch based on its previous run status and frequency.
        
        :param batchid: The batch ID to derive the category for.
        :return: The derived category, either 'LOAD' or 'RERUN'.
        """
        try:
            lastrunrowdet = ''
            crow = ''
            cursor = self.conn.cursor()

            # SQL query to fetch previous run details
            sqlquery = f'''
            SELECT batch_run_id, run_status AS prevrunstatus, 
                   CAST(GETDATE() AS date) AS currdate, 
                   CAST(run_starttime AS date) AS prevrundate,
                   CAST(GETDATE() AS time) AS currtime, 
                   batch_start_time AS batchstarttime, 
                   batch_freq AS frequency
            FROM (
                SELECT batch_id, batch_run_id, run_status, run_starttime, 
                       DENSE_RANK() OVER (ORDER BY run_endtime DESC) rnk
                FROM {configurations.metadb_schema}.tblbatchrundetails
                WHERE batch_id = {batchid}
            ) a, {configurations.metadb_schema}.tblbatchconfig b
            WHERE a.batch_id = b.batch_id AND a.rnk = 1
            '''
            logging.info(sqlquery)
            cursor.execute(sqlquery)

            # Process result
            for lastrunrowdet in cursor:
                crow = lastrunrowdet

            logging.info(f'Last Run Status record found: {lastrunrowdet}')

            # Determine the category based on frequency and status
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
            elif crow.frequency.upper() == 'INTRADAY':
                if crow.prevrunstatus.upper() == configurations.successstatus:
                    category = 'LOAD'
                elif crow.prevrunstatus.upper() == configurations.failstatus:
                    if crow.currtime >= crow.batchstarttime:
                        category = 'LOAD'
                    else:
                        category = 'RERUN'
            return category
        except Exception as e:
            raise Exception(f"{sys._getframe(0).f_code.co_name} : {__name__} : Line {sys.exc_info()[-1].tb_lineno} : {str(e)}")

    def check_lastrun_status(self, batchid):
        """
        Checks the last run status of the batch.
        
        :param batchid: The batch ID to check.
        :return: Tuple of previous batch run ID and status.
        """
        try:
            prevbatchrunid = 0
            prevrunstatus = ''
            cursor = self.conn.cursor()

            # SQL query to get the last run details
            sqlquery = f'''
            SELECT a.* 
            FROM (
                SELECT batch_id, batch_run_id, run_status, 
                       DENSE_RANK() OVER (ORDER BY run_endtime DESC) rnk
                FROM {configurations.metadb_schema}.tblbatchrundetails
                WHERE batch_id = {batchid}
            ) a
            WHERE rnk = 1
            '''
            logging.info(sqlquery)
            cursor.execute(sqlquery)

            # Process result
            for row in cursor:
                prevbatchrunid = row.batch_run_id
                prevrunstatus = row.run_status
                if prevrunstatus == configurations.runningstatus:
                    raise Exception(f"Batch is already running\nBatch Run ID: {prevbatchrunid}\n")
            return prevbatchrunid, prevrunstatus
        except Exception as e:
            raise Exception(f"{sys._getframe(0).f_code.co_name} : {__name__} : Line {sys.exc_info()[-1].tb_lineno} : {str(e)}")

# Example usage:
# metadbconn = connect_to_db()  # Assume this is a valid connection
# batch_processor = BatchProcessor(metadbconn)
# category = batch_processor.derive_runcategory(batchid=123)
# prev_run_id, prev_run_status = batch_processor.check_lastrun_status(batchid=123)
