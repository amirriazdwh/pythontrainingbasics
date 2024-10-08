"""
created by : amir riaz
batchid is the batch of jobs needs to be run.  each batch contains multiple jobs with jobid
loads type can be LOAD and RERUN for full loads jobs. 
you can omitprechecks yes or no
"""

import logging
import argparse
import sessionutils
import prerequisitescheck
import mailmessaging
import batchexecution
import filehandling
import batchdataderiv

class BatchIngestionFramework:
    def __init__(self):
        self.batchname = ''
        self.batchid = None
        self.runcategory = None
        self.omitprereq = None
        self.blogfilename = None
        self.metadbconn = None
        self.btrow = None
        self.prevbatchrunid = None
        self.prevrunstatus = None

    def parse_arguments(self):
        """ Parse command-line arguments """
        parser = argparse.ArgumentParser(description='Datalake Ingestion Framework arguments usage help')
        parser.add_argument('--batchid', type=int, required=True, dest='batch_id',
                            help="Mandatory Parameter. Value of the batch id")
        parser.add_argument('--runcategory', type=str, required=False, choices=['LOAD', 'RERUN'], dest='run_category',
                            help="Optional Parameter. Forces a specific category load to run for the batch")
        parser.add_argument('--omitprechecks', type=str, required=False, choices=['YES', 'NO'], dest='omit_prechecks',
                            help="Optional Parameter. Forces to omit all pre-requisites check for the batch")
        args = parser.parse_args()

        # Store arguments as class attributes
        self.batchid = args.batch_id
        self.runcategory = args.run_category
        self.omitprereq = args.omit_prechecks

    def setup_logging(self):
        """ Set up logging configuration """
        self.blogfilename = sessionutils.setloggingconf(self.batchid)
        logging.info('Logging initialized for batch id: %s', self.batchid)

    def setup_db_connection(self):
        """ Establish connection to Metadata DB """
        self.metadbconn = sessionutils.setmetadbconnmgr()
        logging.info('Metadata DB connection established: %s', self.metadbconn)

    def check_last_run_status(self):
        """ Check the status of the last batch run """
        self.prevbatchrunid, self.prevrunstatus = batchdataderiv.check_lastrun_status(self.batchid, self.metadbconn)
        logging.info('Previous batch run ID: %s, Status: %s', self.prevbatchrunid, self.prevrunstatus)

    def determine_run_category(self):
        """ Derive or use the run category from input arguments """
        if self.runcategory:
            self.batchruntype = self.runcategory
        else:
            self.batchruntype = batchdataderiv.derive_runcategory(self.batchid, self.metadbconn)
            logging.info('Derived run category: %s', self.batchruntype)

    def handle_omit_prechecks(self):
        """ Handle omit pre-checks flag """
        if self.batchruntype == 'RERUN' and self.omitprereq is None:
            self.omitprereq = 'YES'
        logging.info('Omit pre-checks flag: %s', self.omitprereq)

    def run_prerequisites(self):
        """ Run or skip pre-requisite checks """
        if self.omitprereq == 'YES':
            logging.info('Skipping pre-requisite checks')
            self.btrow = prerequisitescheck.get_batch_details(self.batchid, self.metadbconn)
        else:
            logging.info('Running pre-requisite checks')
            self.btrow = prerequisitescheck.prereqmain(self.batchid, self.metadbconn)
            self.batchname = self.btrow.batch_name
            logging.info('Pre-requisite checks completed')

    def execute_batch(self):
        """ Initiate the batch execution """
        logging.info('Initiating batch execution...')
        batchexecution.execmain(self.btrow, self.batchruntype, self.blogfilename, self.metadbconn, self.prevbatchrunid)
        logging.info('Batch execution completed.')

    def send_success_email(self):
        """ Send success email after batch execution """
        logging.info('Sending success email...')
        mailattachmentslist = []
        mailcode = 'BATCHSUCCESS'
        subject = f'Batch Execution Completed: {self.batchname} :: Batch ID: {self.batchid}'
        excelpath, message = batchexecution.get_batchscs_contents(self.btrow.batch_job_count, self.btrow.batch_name, self.btrow.batch_id)
        mailattachmentslist.append(excelpath)
        mailmessaging.send_mail(mailcode, subject, message, mailattachmentslist)
        logging.info('Success email sent.')

    def handle_error(self, e):
        """ Handle errors and send error emails """
        logging.error('Batch execution halted due to error: %s', e)
        mailattachmentslist = []
        if 'BATCHFAILED' in str(e):
            logging.info('Sending batch error email...')
            mailcode = 'BATCHERROR'
            zippath, excelpath, errmessage = batchexecution.get_batchfail_contents(self.btrow.batch_job_count, self.btrow.batch_name,
                                                                                   self.btrow.batch_id, self.blogfilename)
            mailattachmentslist.extend([excelpath, zippath])
            subject = f'Batch Failed: {self.btrow.batch_name}'
            mailmessaging.send_mail(mailcode, subject, errmessage, mailattachmentslist)
        else:
            logging.info('Sending general error email...')
            mailcode = 'OTHERERRORS'
            bloglist = [self.blogfilename]
            if self.batchname:
                blogzip = filehandling.create_zip_file(bloglist, self.batchname)
                subject = f'Batch Failed: {self.batchname} :: Batch ID: {self.batchid}'
            else:
                blogzip = filehandling.create_zip_file(bloglist, str(self.batchid))
                subject = f'Batch Failed for Batch ID: {self.batchid}'
            mailattachmentslist.append(blogzip)
            mailmessaging.send_mail(mailcode, subject, str(e), mailattachmentslist)
        logging.error('Exiting execution due to error.')

    def run(self):
        """ Main execution logic """
        try:
            self.parse_arguments()
            self.setup_logging()
            self.setup_db_connection()
            self.check_last_run_status()
            self.determine_run_category()
            self.handle_omit_prechecks()
            self.run_prerequisites()
            self.execute_batch()
            self.send_success_email()

        except Exception as e:
            self.handle_error(e)

        else:
            logging.info('Batch execution completed successfully.')

# Main execution entry point
if __name__ == "__main__":
    batch_ingestion = BatchIngestionFramework()
    batch_ingestion.run()
