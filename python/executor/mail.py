import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys
from datetime import datetime


def mail(to, cc, message, filename, subject):
    s = smtplib.SMTP(host='192.168.56.102')
    s.starttls()

    msg = MIMEMultipart()
    recipients = to.split(",") + cc.split(",")
    #print recipients

    msg['From'] = 'noreply@test.com'
    msg['To'] = to
    msg['Cc'] = cc
    msg['Subject'] = subject.replace("_", " ")
    msg.attach(MIMEText(message, 'plain'))
    if filename:
        attach_file = open(filename, 'rb')
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(filename, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=basename(filename))
        msg.attach(part)
    s.sendmail('noreply@test.com', recipients, msg.as_string())

    s.quit()


def send_mail(logpath):
    v_to = 'amir@test.com,riaz@test.com'
    v_sub = 'Hadoop Job Success Mail'
    v_from = 'HADOOP-JOB-ALERTS'
    v_msg = """Hello Team,

Hadoop test QC job has succeeded for job : {job_name} .

Please find attached log.

Note: This is an auto generated email alert, please do not reply.

Regards,
Hadoop Team
      """.format(job_name='Query Executor Job', script_name='executor.py', v_error=sys.exc_info()[1],
                 func_name=sys._getframe(1).f_code.co_name)
    if logpath:
        v_to = 'amir@test.com,riaz@test.com'
        v_sub = 'Ingestion Quality Log'
        v_msg = """Hello Team,

Please refer the attached file for Ingestion Quality in tables

Error In Execution Of DQ Config File: None

For any assistance please reach out to amir riaz;

Note: This is an auto generated email alert, please do not reply.

Regards,
Hadoop Team
"""
    v_log_path = '/home/cibg_uat_user/test/qc_framework/output/executor_result_{}.csv'.format(
        datetime.now().strftime('%Y%m%d'))

    mail(v_to, '', v_msg, logpath, v_sub)


def send_Failuremail(logpath):  # failure alert sending module

    if logpath:
        v_to = 'amir@test.com,riaz@test.com'
        v_sub = 'Qc Failed'
        v_msg = """Hello Team,

Please refer the attached file .

QC Failed: Expected count is different than the output.

For any assistance please reach out to amir riaz;

Note: This is an auto generated email alert, please do not reply.

Regards,
Hadoop Team
"""
    v_log_path = '/home/cibg_uat_user/DigiCollect/test/qc_framework/output/executor_result_{}.csv'.format(
        datetime.now().strftime('%Y%m%d'))

    mail(v_to, '', v_msg, logpath, v_sub)
