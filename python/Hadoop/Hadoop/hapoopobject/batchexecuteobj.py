
"""
created by :  Amir Riaz
"""
from pyodbc import connect
from datetime import datetime as date
import os
from time import time, sleep
import sys
import logging
import threading

# Importing Package Libraries
import configurations
import filehandling
import sqoop
import sessionutils
import mailmessaging

# Lock for threading
lock = threading.Lock()

class BatchExecution:
    def __init__(self, runtype, batchlogfullpath, metadbconn):
        """
        Initialize BatchExecution class with necessary attributes.
        """
        self.runtype = runtype
        self.batchlogfullpath = batchlogfullpath
        self.metadbconn = metadbconn
        self.failjobcnt = 0
        self.scsjobcnt = 0
        self.batchrunid = 0

    def exec_main(self, brow, prevbatchrunid):
        """
        Main function to execute the batch run based on run type.
        """
        try:
            # Determine which run category to execute
            if self.runtype.upper() == 'LOAD':
                logging.info('Initiating LOAD Category Run')
                self.exec_batch_init_load(brow)
            elif self.runtype.upper() == 'RERUN':
                logging.info('Initiating RERUN Category Run')
                self.exec_batch_rerun_load(brow, prevbatchrunid)
        except Exception as e:
            raise Exception(f"{sys._getframe(0).f_code.co_name} : {__name__} : Line {sys.exc_info()[-1].tb_lineno} : {str(e)}")

    def exec_batch_init_load(self, brow):
        """
        Executes batch jobs for 'LOAD' category.
        """
        try:
            # Step 1: Create a Batch Run starting entry in the metadata db
            logging.info('Step 1: Create a Batch Run entry and retrieve the batch run id')
            self.batchrunid = self.create_batchrun_record(brow.batch_id)
            logging.info('Batch Run ID generated is %s', self.batchrunid)

            # Step 2: Retrieve jobs details for the batch run
            logging.info('Step 2: Retrieve Jobs Details for the batch')
            jobs = self.get_jobs_for_batch(brow.batch_id)
            logging.info('Job count for this batch: %d', len(jobs))

            # Step 3: Execute each job
            for job in jobs:
                self.execute_job(job)

            # Step 4: Check overall status and finish
            logging.info('Batch Load Execution Completed')

        except Exception as e:
            raise Exception(f"{sys._getframe(0).f_code.co_name} : {__name__} : Line {sys.exc_info()[-1].tb_lineno} : {str(e)}")

    def exec_batch_rerun_load(self, brow, prevbatchrunid):
        """
        Executes batch jobs for 'RERUN' category.
        """
        try:
            # Logic to handle rerun batch jobs
            logging.info('Step 1: Initiate RERUN for batch %s', brow.batch_id)
            # Add further logic similar to exec_batch_init_load

        except Exception as e:
            raise Exception(f"{sys._getframe(0).f_code.co_name} : {__name__} : Line {sys.exc_info()[-1].tb_lineno} : {str(e)}")

    def create_batchrun_record(self, batch_id):
        """
        Creates a new batch run record in the metadata database.
        """
        # Simulated database entry
        logging.info('Creating batch run record for batch ID: %s', batch_id)
        # Simulated batch run ID
        return 12345

    def get_jobs_for_batch(self, batch_id):
        """
        Retrieve the jobs for the specified batch ID.
        """
        # Simulated jobs list
        logging.info('Fetching jobs for batch ID: %s', batch_id)
        return [{'job_id': 1, 'job_name': 'Job1'}, {'job_id': 2, 'job_name': 'Job2'}]

    def execute_job(self, job):
        """
        Execute individual job.
        """
        logging.info('Executing job: %s', job['job_name'])
        # Simulate job execution
        sleep(1)
        logging.info('Job %s completed', job['job_name'])

# Example usage:
# batch_execution = BatchExecution(runtype='LOAD', batchlogfullpath='/path/to/log', metadbconn='DB connection object')
# batch_execution.exec_main(brow_object, prevbatchrunid=1234)
