"""
Module Name : batchint.py
Created On  : 10th Nov 2019
Created By  : Amir Riaz
Purpose     : Main module for batch execution in the Ingestion Framework
"""

# Importing necessary Python libraries
import logging
import sys
import argparse

# Importing custom modules for batch processing
import sessionutils
import prerequisitescheck
import mailmessaging
import batchexecution
import filehandling
import batchdataderiv

try:
    # Initializing variables
    batchname = ''

    # Setting up command-line argument parser
    parser = argparse.ArgumentParser(description='Datalake Ingestion Framework argument help')
    parser.add_argument('--batchid', type=int, required=True, dest='batch_id',
                        help="Mandatory Parameter: Batch ID")
    parser.add_argument('--runcategory', type=str, required=False, choices=['LOAD', 'RERUN'], dest='run_category', 
                        help="Optional Parameter: Specify the category (LOAD or RERUN) to run")
    parser.add_argument('--omitprechecks', type=str, required=False, choices=['YES', 'NO'], dest='omit_prechecks', 
                        help="Optional Parameter: Skip pre-requisite checks (YES or NO)")
    args = parser.parse_args()

    # Storing argument values into variables
    batchid = args.batch_id
    runcategory = args.run_category
    omitprereq = args.omit_prechecks

    # Configuring logging for the batch execution
    blogfilename = sessionutils.setloggingconf(batchid)
    logging.info('Starting batch execution for ID %s, category %s, omit pre-checks: %s', batchid, runcategory, omitprereq)

    # Establishing a connection to the metadata database
    logging.info('Setting up Metadata DB connection...')
    metadbconn = sessionutils.setmetadbconnmgr()
    logging.info('Metadata DB connection established: %s', metadbconn)

    # Checking the status of the last batch run
    prevbatchrunid, prevrunstatus = batchdataderiv.check_lastrun_status(batchid, metadbconn)
    logging.info('Previous batch run ID: %s, status: %s', prevbatchrunid, prevrunstatus)

    # Determine the batch run type (LOAD or RERUN)
    if runcategory is None:
        batchruntype = batchdataderiv.derive_runcategory(batchid, metadbconn)
        logging.info('Run category derived as: %s', batchruntype)
    else:
        batchruntype = runcategory

    # Automatically set omit pre-requisite checks to 'YES' if batch type is RERUN and not provided
    if batchruntype == 'RERUN' and omitprereq is None:
        omitprereq = 'YES'
        logging.info('Omit pre-requisite flag set to: %s', omitprereq)

    # Execute pre-requisite checks if not omitted
    if omitprereq == 'YES':
        logging.info('Skipping pre-requisite checks...')
        btrow = prerequisitescheck.get_batch_details(batchid, metadbconn)
    else:
        logging.info('Running pre-requisite checks...')
        btrow = prerequisitescheck.prereqmain(batchid, metadbconn)
        batchname = btrow.batch_name
        logging.info('Pre-requisite checks completed successfully')

    # Begin batch execution
    logging.info('Starting batch execution...')
    batchexecution.execmain(btrow, batchruntype, blogfilename, metadbconn, prevbatchrunid)
    logging.info('Batch execution completed. Preparing success summary email...')

    # Send a success email with summary
    mailattachmentslist = []
    mailcode = 'BATCHSUCCESS'
    subject = f'Batch Execution Completed: {batchname} :: Batch ID: {batchid}'
    excelpath, message = batchexecution.get_batchscs_contents(btrow.batch_job_count, btrow.batch_name, btrow.batch_id)
    mailattachmentslist.append(excelpath)
    mailmessaging.send_mail(mailcode, subject, message, mailattachmentslist)
    logging.info('Success email sent.')

except Exception as e:
    logging.error('Batch execution halted due to an error: %s', e)

    # Sending error email in case of failure
    mailattachmentslist = []
    if 'BATCHFAILED' in str(e):
        logging.info('Sending detailed batch error email...')
        mailcode = 'BATCHERROR'
        zippath, excelpath, errmessage = batchexecution.get_batchfail_contents(btrow.batch_job_count, btrow.batch_name,
                                                                               btrow.batch_id, blogfilename)
        mailattachmentslist.extend([excelpath, zippath])
        subject = f'Batch Failed: {btrow.batch_name}'
        mailmessaging.send_mail(mailcode, subject, errmessage, mailattachmentslist)
    else:
        logging.info('Sending generic error email...')
        mailcode = 'OTHERERRORS'
        bloglist = [blogfilename]
        if batchname:
            blogzip = filehandling.create_zip_file(bloglist, batchname)
            subject = f'Batch Failed: {batchname} :: Batch ID: {batchid}'
        else:
            blogzip = filehandling.create_zip_file(bloglist, str(batchid))
            subject = f'Batch Failed for Batch ID: {batchid}'
        mailattachmentslist.append(blogzip)
        mailmessaging.send_mail(mailcode, subject, e, mailattachmentslist)

    logging.error('Exiting batch execution...')
else:
    logging.info('Batch execution completed successfully.')
finally:
    pass
