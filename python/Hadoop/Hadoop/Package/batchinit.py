'''
Module Name : batchint.py
Created On : 10th Nov 2019
Created By : amir riaz
Purpose : This module is the main entry module for a batch execution in Ingestion Framework
'''

#Importing Python Libraries
import logging
import sys
import argparse

#Importing Package Modules
import sessionutils
import prerequisitescheck 
import mailmessaging
import batchexecution
import filehandling
import batchdataderiv

#Initiating the batch
try:
    batchname = ''
    #Script arguments 
    parser = argparse.ArgumentParser(description= 'Datalake Ingestion Framework arguments usage help')
    parser.add_argument('--batchid', type=int, required=True, dest='batch_id',help="Mandatory Parameter. Value of the batch id")
    parser.add_argument('--runcategory', type=str, required=False,choices=['LOAD','RERUN'], dest='run_category', help="Optional Parameter. \
                        Forces a specific category load to run for the batch")
    parser.add_argument('--omitprechecks', type=str, required=False,choices=['YES','NO'], dest='omit_prechecks', help="Optional Parameter. \
                        Forces to omit all pre-requisites check for the batch")
    args = parser.parse_args()

    #Assigning values to variables from the passed arguments values
    batchid = args.batch_id
    runcategory = args.run_category
    omitprereq = args.omit_prechecks

    #Setting the Logging Configurations
    blogfilename = sessionutils.setloggingconf(batchid)
    logging.info('Starting Logging for batch id %s, runcategory %s, omitprereq %s',batchid,runcategory,omitprereq)  

    #Setting the metadb connection variable
    logging.info('Setting Metadata DB Connection Variable')
    metadbconn = sessionutils.setmetadbconnmgr()
    logging.info('metadbconn : %s', metadbconn)

    #Checking last run status
    prevbatchrunid,prevrunstatus = batchdataderiv.check_lastrun_status(batchid,metadbconn)
    logging.info('Previous Batch Run ID is %s and Previous Batch Run Status is %s',prevbatchrunid,prevrunstatus)

    #Derive the Run Category
    if runcategory != None:
        batchruntype = runcategory
    else:
        batchruntype = batchdataderiv.derive_runcategory(batchid,metadbconn)
        logging.info('Derived Run Category is %s',batchruntype)  

    #Update the omit pre-requisites flag
    if batchruntype == 'RERUN' and omitprereq == None:
        omitprereq = 'YES'
        logging.info('Omit Pre-requisites flag updated as %s',omitprereq) 

    #Running the pre-requisites check
    if omitprereq == 'YES':
        logging.info('Pre-requisites check omitted. Values for omitprereq argument was %s',omitprereq)
        btrow = prerequisitescheck.get_batch_details(batchid,metadbconn)
    else: 
        logging.info('Running Pre-Requisites checks')
        btrow = prerequisitescheck.prereqmain(batchid,metadbconn)
        batchname = btrow.batch_name
        logging.info('Pre-requisites check completed successfully')

    #Initiating the batch execution
    logging.info('Initiating Batch Execution') 
    batchexecution.execmain(btrow,batchruntype,blogfilename,metadbconn,prevbatchrunid)            
    logging.info('Batch Execution Completed. Sending Summary Mail')

    #Sending Batch Success Email
    mailattachmentslist = []
    mailcode = 'BATCHSUCCESS'
    subject = 'Batch Execution Completed : ' + batchname + ' :: Batch ID : ' + str(batchid) 
    excelpath, message = batchexecution.get_batchscs_contents(btrow.batch_job_count,btrow.batch_name,btrow.batch_id)
    mailattachmentslist.append(excelpath)
    mailmessaging.send_mail(mailcode,subject,message,mailattachmentslist)
    logging.info('Success Summary Mail Sent')

except Exception as e:
    logging.error('Batch Execution Halted due to some error')
    logging.error(e)

    #Sending error mails
    mailattachmentslist = []
    if str(e).find('BATCHFAILED') != -1:
        logging.info('Starting to send the Batch error detailed email')
        mailcode = 'BATCHERROR'
       #brunid = str(e).split(' ')[-1]
        zippath, excelpath, errmessage = batchexecution.get_batchfail_contents(btrow.batch_job_count,btrow.batch_name,btrow.batch_id,blogfilename) 
        mailattachmentslist.append(excelpath)
        mailattachmentslist.append(zippath)
        subject = 'Batch Failed for ' + btrow.batch_name
        mailmessaging.send_mail(mailcode,subject,errmessage,mailattachmentslist)
    else:
        logging.info('Starting to send the other error email')
        mailcode = 'OTHERERRORS'
        bloglist = [blogfilename]
        if batchname != '':
            blogzip = filehandling.create_zip_file(bloglist,batchname)
            mailattachmentslist.append(blogzip)
            subject = 'Batch Failed : ' + batchname + ' :: Batch ID : ' + str(batchid) 
        else:
            blogzip = filehandling.create_zip_file(bloglist,str(batchid))
            mailattachmentslist.append(blogzip)
            subject = 'Batch Failed for Batch ID : ' + str(batchid)
        mailmessaging.send_mail(mailcode,subject,e,mailattachmentslist)
            
    logging.error('Exiting the execution')
else:
    logging.info('Batch Execution Completed Sucessfully')
finally:
    pass



