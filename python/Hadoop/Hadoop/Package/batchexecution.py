'''
Module Name : batchexecution.py
Created On : 10th Nov 2019
Created By : Amir Riaz
Purpose : This module caters with running the requested batch execution
'''

# Importing Python Libraries
from pyodbc import connect
from datetime import datetime as date
import os
from time import time, sleep
import sys
import logging
import Queue as queue
import threading

# Importing Package Libraries
import configurations
import filehandling
import sqoop
import sessionutils
import mailmessaging

# global variables
runtype = ''
batchlogfullpath = ''
metadbconn = ''
failjobcnt = 0
scsjobcnt = 0
batchrunid = 0
lock = threading.Lock()


# main function of the module
def execmain(brow, bruntype, blogpath, metadb, prevbatchrunid):
    global runtype, batchlogfullpath, metadbconn
    try:
        # Assigning variables to be used in the module
        runtype = bruntype
        batchlogfullpath = blogpath
        metadbconn = metadb

        # Calling the respective load based on the run category
        if runtype.upper() == 'LOAD':
            logging.info('Initiating LOAD Category Run')
            execbatchinitload(brow)
        elif runtype.upper() == 'RERUN':
            logging.info('Initiating RERUN Category Run')
            execbatchrerunload(brow, prevbatchrunid)
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))

    # Function for LOAD category batch execution


def execbatchinitload(brow):
    global runtype, batchlogfullpath, metadbconn, failjobcnt, scsjobcnt, batchrunid
    try:
        # Creating a Batch Run starting entry in the metadata db
        logging.info('Step 1 : Create a Batch Run entry and retrieve the batch run id')
        batchrunid = create_batchrun_record(brow.batch_id, runtype, batchlogfullpath, metadbconn)
        logging.info('Batch Run ID generated is %s', batchrunid)

        # Getting the jobs detail of the running batch id
        logging.info('Step 2 : Get the job details for the batch id')
        jdatacur = get_initjob_details(brow.batch_id, metadbconn)

        logging.info('Step 3 : Initializing the batch counter variable j as 1')
        j = 1

        logging.info('Step 4 : Starting the batch execution')
        logging.info('Session value of jobfailthreshold is %s, parallelism is %s', brow.batch_jobfail_threshold,
                     brow.batch_parallelism)

        start = time()
        q = queue.Queue(maxsize=0)

        # Till the time job failure count stays less than the batch threshhold, the below loop will work
        while failjobcnt <= brow.batch_jobfail_threshold:
            try:
                for i in range(brow.batch_parallelism):
                    t = threading.Thread(target=executejob, args=(q, brow, batchrunid))
                    t.setDaemon(True)
                    t.start()
                for x in jdatacur:
                    q.put(x)
                    logging.info('putting x value %s', x)
                q.join()
                break
            except Exception as e:
                logging.error(e)
            continue
        end = time()
        logging.info('Jobs execution completed with failed jobs count as %s', failjobcnt)

        # if any jobs failed in the batch, then mark the batch as failed else success
        if failjobcnt != 0:
            logging.error('Batch Execution failed with success jobs count as %s and failed jobs count as %s', scsjobcnt,
                          failjobcnt)
            logging.error('Total Time taken in batch execution is : %s', end - start)
            raise Exception('FAILEXCEPTION')
        else:
            logging.info('Batch Completed Successfully')
            logging.info('Total Time taken in batch execution is : %s', str(end - start))
            update_batchrun_record(batchrunid, configurations.successstatus, scsjobcnt, failjobcnt, metadbconn)
    except Exception as e:
        logging.error(e)
        logging.error(batchrunid)

        # Sending custom exception so that batch main function can decide to send a summary mail or not
        if str(e) == 'FAILEXCEPTION':
            update_batchrun_record(batchrunid, configurations.failstatus, scsjobcnt, failjobcnt, metadbconn)
            raise Exception('BATCHFAILED' + ' ' + str(batchrunid))
        elif batchrunid != '':
            update_batchrun_record(batchrunid, configurations.failstatus, scsjobcnt, failjobcnt, metadbconn)
            raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
                sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))
        else:
            raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
                sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))

        # Function for RERUN category batch execution


def execbatchrerunload(brow, prevbatchrunid):
    global runtype, batchlogfullpath, metadbconn, failjobcnt, scsjobcnt, batchrunid
    try:
        # Creating a Batch Run starting entry in the metadata db
        logging.info('Step 1 : Create a Batch Run entry and retrieve the batch run id')
        batchrunid = create_batchrun_record(brow.batch_id, runtype, batchlogfullpath, metadbconn)
        logging.info('Batch Run ID generated is %s', batchrunid)

        # Getting the jobs detail of the running batch id
        logging.info('Step 2 : Get the job details for rerun for the batch id')
        jdatacur = get_rerunjob_details(brow.batch_id, metadbconn, prevbatchrunid)

        logging.info('Step 3 : Initializing the batch counter variable j as 1')
        j = 1

        logging.info('Step 4 : Starting the batch execution')
        logging.info('Session value of jobfailthreshold is %s, parallelism is %s', brow.batch_jobfail_threshold,
                     brow.batch_parallelism)

        start = time()
        q = queue.Queue(maxsize=0)

        # Till the time job failure count stays less than the batch threshhold, the below loop will work
        while failjobcnt <= brow.batch_jobfail_threshold:
            try:
                for i in range(brow.batch_parallelism):
                    t = threading.Thread(target=executejob, args=(q, brow, batchrunid))
                    t.setDaemon(True)
                    t.start()
                for x in jdatacur:
                    q.put(x)
                q.join()
                break
            except Exception as e:
                logging.error(e)
            continue
        end = time()
        logging.info('Jobs execution completed with failed jobs count as %s', failjobcnt)

        # if any jobs failed in the batch, then mark the batch as failed else success
        if failjobcnt != 0:
            logging.error('Batch Execution failed with success jobs count as %s and failed jobs count as %s', scsjobcnt,
                          failjobcnt)
            logging.error('Total Time taken in batch execution is : %s', end - start)
            raise Exception('FAILEXCEPTION')
        else:
            logging.info('Batch Completed Successfully')
            logging.info('Total Time taken in batch execution is : %s', str(end - start))
            update_batchrun_record(batchrunid, configurations.successstatus, scsjobcnt, failjobcnt, metadbconn)
    except Exception as e:
        logging.error(e)
        logging.error(batchrunid)

        # Sending custom exception so that batch main function can decide to send a summary mail or not
        if str(e) == 'FAILEXCEPTION':
            update_batchrun_record(batchrunid, configurations.failstatus, scsjobcnt, failjobcnt, metadbconn)
            raise Exception('BATCHFAILED' + ' ' + str(batchrunid))
        elif batchrunid != '':
            update_batchrun_record(batchrunid, configurations.failstatus, scsjobcnt, failjobcnt, metadbconn)
            raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
                sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))
        else:
            raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
                sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))

        # Function to get the batch details against a batch id


def create_batchrun_record(batchid, runtype, logpath, metadbconn):
    try:
        logging.info('Inserting the record in tblbatchrundetails')
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'INSERT INTO {}.tblbatchrundetails (batch_id,run_category,run_starttime,run_status,run_logpath) VALUES({},{},getdate(),{},{})' \
            .format(configurations.metadb_schema, batchid, "'" + runtype + "'",
                    "'" + configurations.runningstatus + "'", "'" + logpath + "'")
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        conn.commit()
        cursor.execute('SELECT @@IDENTITY')
        batchrunid = cursor.fetchone()[0]
        logging.info('Batch Run ID %s created for this batch execution ', batchrunid)
        return batchrunid
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to get the jobs details of a batch
def get_initjob_details(batchid, metadbconn):
    try:
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'select * from {}.tbljobconfig where batch_id = {} order by load_priority'.format(
            configurations.metadb_schema, batchid)
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        return cursor
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to get the rerun job details of a batch
def get_rerunjob_details(batchid, metadbconn, prevbatchrunid):
    try:
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'select a.* from {}.tbljobconfig a where job_id in \
                        (select job_id from {}.tbljobrundetails where batch_run_id = {} and run_status = {} )\
                        and batch_id = {} \
                        order by load_priority'.format(configurations.metadb_schema, configurations.metadb_schema, \
                                                       prevbatchrunid, "'" + configurations.failstatus + "'", batchid)
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        return cursor
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to update the batch run record
def update_batchrun_record(batchrunid, status, scsjobcnt, failjobcnt, metadbconn):
    try:
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'UPDATE {}.tblbatchrundetails \
                        set run_endtime = getdate(), run_status={}, \
                        total_time_in_sec = DATEDIFF(SECOND, run_starttime, getdate()) , success_job_count ={}, fail_job_count={} \
                        where batch_run_id = {}'.format(configurations.metadb_schema, "'" + status + "'", scsjobcnt,
                                                        failjobcnt, batchrunid)
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        conn.commit()
        logging.info('Batch Run ID record updated for run id %s with status %s and success count %s and fail count %s' \
                     , batchrunid, status, scsjobcnt, failjobcnt)
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to execute the job
def executejob(q, brow, batchrunid):
    while True:
        global failjobcnt, scsjobcnt
        try:
            jdatarow = q.get()
            threadid = threading.currentThread().ident
            threadname = threading.currentThread().getName()
            thmetadbconn = sessionutils.setmetadbconnmgr()

            print('the job id picked is' + str(jdatarow))

            logging.info('Job ID: %s, Thread ID & Name: %s & %s :: starting execution', jdatarow.job_id, threadid,
                         threadname)
            jobrunid = create_jobrun_record(brow.batch_id, batchrunid, jdatarow.job_id, thmetadbconn)
            logging.info('Job ID: %s, Thread ID & Name: %s & %s :: created job run entry as %s', jdatarow.job_id,
                         threadid, threadname, jobrunid)

            # Getting the sqoop log path
            jobname = jdatarow.dest_schema + '_' + jdatarow.dest_obj_name
            sqplogpath = sessionutils.getsqooplogpath(jobrunid, jobname)
            sqpjobcrlogpath = sessionutils.getsqoopjobcrlogpath(jobrunid, jobname)
            avroexeclogpath = sessionutils.avroexeclogpath(jobrunid, jobname)
            logging.info('Job ID: %s, Thread ID & Name: %s & %s :: sqoop log path is %s', jdatarow.job_id, threadid,
                         threadname, sqplogpath)

            j = 1
            while j <= brow.batch_retry_count:
                try:
                    attachmentslist = []
                    # Initiating execution and initializing variables
                    logging.info('Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: starting execution',
                                 jdatarow.job_id, threadid, threadname, j)
                    prescriptstatus = ''
                    sqooploadstatus = ''
                    postscriptstatus = ''

                    # If the job has a pre-script then run the same else ignore
                    if jdatarow.pre_run_script != None:
                        try:
                            sout, serr, returncode = sessionutils.rununixcommand(jdatarow.pre_run_script)
                            if returncode != 0:
                                raise Exception(serr)
                            else:
                                prescriptstatus = 'S'
                                logging.info(
                                    'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: pre-script execution completed with output :',
                                    jdatarow.job_id, threadid, threadname, j)
                                logging.info(sout)
                        except Exception as e:
                            prescriptstatus = 'F'
                            logging.error(
                                'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: pre-script execution failed with error :',
                                jdatarow.job_id, threadid, threadname, j)
                            logging.error(e)
                            raise Exception(e)
                    else:
                        # Status None for pre script means that prescript was not applicable for this job
                        prescriptstatus = None
                        logging.info('Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: no pre-script found',
                                     jdatarow.job_id, threadid, threadname, j)

                    # Run the sqoop command for the job
                    try:
                        sqpcmd, sqpexeccmd = sqoop.gen_sqoop_command(jdatarow, brow, metadbconn, jobrunid, sqplogpath)
                        logging.info(
                            'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: generated sqoop command is %s',
                            jdatarow.job_id, threadid, threadname, j, sqpcmd.replace('....', ' '))

                        if jdatarow.incremental_key != None:
                            jobcreatecode = sessionutils.rununixcommand(sqpcmd.replace('....', ' '), sqpjobcrlogpath)
                            jobexeccode = sessionutils.rununixcommand(sqpexeccmd.replace('....', ' '), sqplogpath)
                            if jobcreatecode != 0 or jobexeccode != 0:
                                linefoundstat = sqoop.chk_incr_zerorec(sqplogpath)
                                if linefoundstat == 1:
                                    sqooploadstatus = 'S'
                                else:
                                    raise Exception('Sqoop Command failed with error return code. check sqoop log')
                            else:
                                sqooploadstatus = 'S'

                        elif jdatarow.file_formats.upper() == 'AVRO':
                            jobexeccode = sessionutils.rununixcommand(sqpcmd.replace('....', ' '), sqplogpath)
                            tblhivcode = sessionutils.rununixcommand(sqpexeccmd.replace('....', ' '), avroexeclogpath)
                            if jobexeccode != 0 or tblhivcode != 0:
                                raise Exception('Sqoop Command failed with error return code. check sqoop log')
                            else:
                                sqooploadstatus = 'S'
                        else:
                            jobexeccode = sessionutils.rununixcommand(sqpcmd.replace('....', ' '), sqplogpath)
                            if jobexeccode != 0:
                                raise Exception('Sqoop Command failed with error return code. check sqoop log')
                            else:
                                sqooploadstatus = 'S'

                        if sqooploadstatus == 'S':
                            logging.info(
                                'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: sqoop execution completed successfully',
                                jdatarow.job_id, threadid, threadname, j)

                            # Get the rows impacted by the sqoop command
                            reccnt = sqoop.get_records_count(sqplogpath)
                            logging.info(
                                'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: sqoop execution records retrived as %s',
                                jdatarow.job_id, threadid, threadname, j, reccnt)
                    except Exception as e:
                        if os.path.exists(sqplogpath):
                            attachmentslist.append(sqplogpath)
                            sqooploadstatus = 'F'
                            logging.error('Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: sqoop command run failed with sqplog and error : %s \
                                            check sqoop log file', jdatarow.job_id, threadid, threadname, j, e)
                        else:
                            sqooploadstatus = None
                            logging.error('Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: sqoop command run failed with no sqplog and error : %s \
                                            check sqoop log file', jdatarow.job_id, threadid, threadname, j, e)
                        raise Exception(e)

                    # If the job has a pre-script then run the same else ignore
                    if jdatarow.post_run_script != None:
                        try:
                            sout, serr, returncode = sessionutils.rununixcommand(jdatarow.post_run_script)
                            if returncode != 0:
                                raise Exception(serr)
                            else:
                                postscriptstatus = 'S'
                                logging.info(
                                    'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: post-script execution completed with output :',
                                    jdatarow.job_id, threadid, threadname, j)
                                logging.info(sout)
                        except Exception as e:
                            postscriptstatus = 'F'
                            logging.error(
                                'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: post-script execution failed with error :',
                                jdatarow.job_id, threadid, threadname, j)
                            logging.error(e)
                            raise Exception(e)
                    else:
                        # Status None for pre script means that postscript was not applicable for this job
                        postscriptstatus = None
                        logging.info('Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: no post-script found',
                                     jdatarow.job_id, threadid, threadname, j)

                    update_jobrun_record(jobrunid, configurations.successstatus, reccnt, thmetadbconn, sqplogpath,
                                         prescriptstatus, sqooploadstatus, postscriptstatus)
                    logging.info(
                        'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: updated job run id with status as success',
                        jdatarow.job_id, threadid, threadname, j)

                    # Updating the batch success job count
                    with lock:
                        scsjobcnt += 1
                        logging.info(
                            'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: updated success job count to %s',
                            jdatarow.job_id, threadid, threadname, j, scsjobcnt)
                    break
                except Exception as e:
                    # Identifying the number of failed attempt and deriving the run needs to be done again
                    if j >= brow.batch_retry_count:
                        logging.info(
                            'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: retries attempt exceeded. job failed',
                            jdatarow.job_id, threadid, threadname, j)
                        logging.error(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
                            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))

                        # Updating the job as failed as all retry attempts have failed
                        update_jobrun_record(jobrunid, configurations.failstatus, 0, thmetadbconn, sqplogpath,
                                             prescriptstatus, sqooploadstatus, postscriptstatus)
                        # Updating the batch fail job count
                        with lock:
                            failjobcnt += 1
                        # Sending Job Failure email
                        logging.info(
                            'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: sending job failure mail',
                            jdatarow.job_id, threadid, threadname, j)
                        send_job_failemail(attachmentslist, brow.batch_name, jobname, e)
                        logging.info('Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: Mail sent',
                                     jdatarow.job_id, threadid, threadname, j)
                        raise Exception(e)
                    else:
                        logging.error(e)
                        logging.info(
                            'Job ID: %s, Thread ID & Name: %s & %s, Attempt No: %s :: execution failed. Initiating the next try after %s seconds', \
                            jdatarow.job_id, threadid, threadname, j, brow.batch_retry_waittime_sec)

                        # Increase the counter value for retry and sleep for wait time
                        j += 1
                        sleep(brow.batch_retry_waittime_sec)
                continue
        except Exception as e:
            print('caught an exception' + str(e))
            # raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(sys.exc_info()[-1].tb_lineno)  + ' : ' + str(e))
        finally:
            q.task_done()


# Function to create a record for job run
def create_jobrun_record(batchid, batchrunid, job_id, metadbconn):
    try:
        logging.info('Inserting the record in tbljobrundetails')
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'INSERT INTO {}.tbljobrundetails \
                            (batch_id,batch_run_id,job_id,run_starttime,run_status) \
                            VALUES \
                            ({},{},{},getdate(),{})'.format(configurations.metadb_schema, batchid, batchrunid, job_id,
                                                            "'" + configurations.runningstatus + "'")
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        conn.commit()
        cursor.execute('SELECT @@IDENTITY')
        jobrunid = cursor.fetchone()[0]
        logging.info('Job Run ID %s created for this job execution', job_id)
        return jobrunid
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to update the record for running job with the respective status
def update_jobrun_record(jobrunid, status, reccnt, metadbconn, sqplogpath, prescriptstatus, sqooploadstatus,
                         postscriptstatus):
    try:
        conn = metadbconn
        cursor = conn.cursor()

        if prescriptstatus != None:
            prestat = "'" + prescriptstatus + "'"
        else:
            prestat = "''"

        if postscriptstatus != None:
            poststat = "'" + postscriptstatus + "'"
        else:
            poststat = "''"

        sqlquery = 'UPDATE {}.tbljobrundetails \
                        set run_endtime = getdate(), run_status={}, \
                        total_time_in_sec = DATEDIFF(SECOND, run_starttime, getdate()) , row_count ={}, job_logpath={}, \
                        prescriptstatus = {}, sqoopstatus = {}, postscriptstatus = {} \
                        where job_run_id = {}'.format(configurations.metadb_schema, "'" + status + "'", reccnt,
                                                      "'" + sqplogpath + "'", \
                                                      prestat, "'" + sqooploadstatus + "'", poststat, jobrunid)
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        conn.commit()
        logging.info('Job Run ID Details updated in the table %s with status as %s', jobrunid, status)
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to create the attachment content to send in the batch failure mail
def get_batchfail_contents(totaljobcount, batchname, batchid, blogfilename):
    try:
        global scsjobcnt, failjobcnt, batchrunid
        failedjobslogpathlist = get_failedjobs_logpaths(batchrunid, blogfilename)
        logging.info('Failed Jobs Log list length is %s', len(failedjobslogpathlist))
        zipfilefullpath = ''
        if len(failedjobslogpathlist) != 0:
            zipfilefullpath = filehandling.create_zip_file(failedjobslogpathlist, batchname)
        excelfilefullpath = filehandling.create_excel_file(metadbconn, batchname, batchrunid)
        failmessage = 'Batch Name : ' + batchname + '\n' + \
                      'Batch ID : ' + str(batchid) + '\n' + \
                      'Batch Run ID: ' + str(batchrunid) + '\n' + \
                      'Total Number of jobs in the batch : ' + str(totaljobcount) + '\n' + \
                      'Success Jobs : ' + str(scsjobcnt) + '\n' + \
                      'Failed Jobs : ' + str(failjobcnt) + '\n'
        return zipfilefullpath, excelfilefullpath, failmessage
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))

    # Function to get the jobs logs list for the failed jobs


def get_failedjobs_logpaths(batchrunid, blogfilename):
    try:
        global metadbconn
        conn = metadbconn
        cursor = conn.cursor()
        sqlquery = 'Select job_logpath from {}.tbljobrundetails where batch_run_id = {} and run_status = {}'.format(
            configurations.metadb_schema, \
            batchrunid, "'" + configurations.failstatus + "'")
        logging.info(sqlquery)
        cursor.execute(sqlquery)
        loglist = []
        loglist.append(blogfilename)
        for row in cursor:
            if row[0] != None and row[0] != '':
                loglist.append(row[0])
        return loglist
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


def send_job_failemail(mailattachmentslist, batchname, jobname, error):
    try:
        mailcode = ''
        subject = 'Job Failed : ' + batchname + ' : ' + jobname
        if mailattachmentslist == []:
            message = 'Job Failed with error : ' + str(error)
        else:
            message = 'Please check the attached sqoop log file for error'
        mailmessaging.send_mail(mailcode, subject, message, mailattachmentslist)
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to create the attachment content to send in the batch failure mail
def get_batchscs_contents(totaljobcount, batchname, batchid):
    try:
        global scsjobcnt, failjobcntm, batchrunid
        excelfilefullpath = filehandling.create_excel_file(metadbconn, batchname, batchrunid)
        scsmessage = 'Batch Name : ' + batchname + '\n' + \
                     'Batch ID : ' + str(batchid) + '\n' + \
                     'Batch Run ID: ' + str(batchrunid) + '\n' + \
                     'Total Number of jobs in the batch : ' + str(totaljobcount) + '\n' + \
                     'Success Jobs : ' + str(scsjobcnt) + '\n'
        return excelfilefullpath, scsmessage
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))
