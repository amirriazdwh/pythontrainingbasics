'''
Module Name : mailmessaging.py
Created On : 10th Nov 2019
Created By : amir riaz
Purpose : This module is for mail messaging functionalities related functions called at certain stages
'''

#Importing Python Libraries 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import logging
import sys
from os.path import basename

#Importing Package Modules
import configurations

def send_mail(mailcode,subject,errdetails,attachmentslist):
    try:
        server = ''
        sent_from = configurations.from_mail
        to_list = configurations.to_mail
        cc_list = configurations.cc_mail
        to_mail = to_list + cc_list
        un_to_mail = list(set(to_mail))

        #Creating message object and attaching the body
        msg = MIMEMultipart()
        msg['From'] = sent_from
        msg['To'] = ",".join(to_list)
        msg['Cc'] = ",".join(cc_list)
        msg['Subject'] = subject
        body = get_msg_body(mailcode, errdetails ,len(attachmentslist))
        msg.attach(MIMEText(body,'plain'))

        #Checking for attachments and if available then attaching the same
        for attachment in attachmentslist:
            logging.info('Attaching file %s', attachment)
            filefullname = attachment
            file = open(filefullname, 'rb')
            p = MIMEBase('application','octet-stream')
            p.set_payload(file.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition','attachment', filename = basename(filefullname))
            msg.attach(p)

        #Sending the mail
        emailmessage = msg.as_string()
        server = smtplib.SMTP(configurations.smtp_server)
        server.sendmail(sent_from,un_to_mail,emailmessage)
        logging.info(un_to_mail)
        logging.info('Mail Sent')
    except Exception as e:
        logging.error(e)
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(sys.exc_info()[-1].tb_lineno)  + ' : ' + str(e))
    finally:
        if server != '': server.quit()

def get_msg_body(code, errdet, attachments):
    try:
        #Deriving end message variable
        if attachments != 0:
            endmessage = 'Further details of failed jobs can be checked via attachments of this email. Please check the error and resolve'
        else:
            endmessage = 'Please check the error and resolve'

        #Deriving the body content of the email
        if code.upper() == 'BATCHERROR':
            body = 'Hi Team,' + '\n' + '\n' \
                    + 'Error occurred with the batch run. Below is the brief summary' + '\n' + '\n' \
                    + str(errdet) + '\n' + '\n' \
                    + endmessage + '\n' + '\n' \
                    + 'Regards,' + '\n' \
                    + 'Hadoop Prod Support Team'
        elif code.upper() == 'BATCHSUCCESS':
            body = 'Hi Team,' + '\n' + '\n' \
                    + 'Batch execution completed successfully. Below is the brief summary' + '\n' + '\n' \
                    + str(errdet) + '\n' + '\n' \
                    + 'Regards,' + '\n' \
                    + 'Hadoop Prod Support Team'
        else:    
            body = 'Hi Team,' + '\n' + '\n' \
                    + 'Error occurred in the batch run with the below error : ' + '\n' + '\n' \
                    + str(errdet) + '\n' + '\n' \
                    + endmessage + '\n' + '\n' \
                    + 'Regards,' + '\n' \
                    + 'Hadoop Prod Support Team'
        return body
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(sys.exc_info()[-1].tb_lineno)  + ' : ' + str(e))



