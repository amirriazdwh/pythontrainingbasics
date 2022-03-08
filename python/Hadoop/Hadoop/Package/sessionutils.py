'''
Module Name : sessionutils.py
Created On : 10th Nov 2019
Created By : Amir Riaz
Purpose : This module caters with defining session level settings of each batch run
'''

# Importing Python Libraries
import logging
from datetime import datetime as date
from pyodbc import connect
import sys
import subprocess
import Crypto
from Crypto.Cipher import ARC4
import base64

# Importing Package Modules
import configurations


# Function to set logging properties
def setloggingconf(batchid):
    try:
        logfilefullname = configurations.logging_dir + configurations.logging_file_name_init \
                          + str(batchid) + '_' \
                          + str(date.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '') \
                          + configurations.logging_file_format
        logging.basicConfig(filename=logfilefullname, \
                            format='%(asctime)s %(levelname)-8s %(message)s', \
                            filemode='w', \
                            level=logging.DEBUG)
        return logfilefullname
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


# Function to set connection variable for Hadoop Metadata DB for the current session
def setmetadbconnmgr():
    try:
        connstring = 'Driver={' + configurations.metadb_driver + '};' \
                     + 'Server=' + configurations.metadb_server + ';' \
                     + 'Database=' + configurations.metadb_name + ';' \
                     + 'UID=' + configurations.metadb_username + ';' \
                     + 'PWD=' + configurations.metadb_password + ';'
        conn = connect(connstring)
        return conn
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


def getsqooplogpath(jrunid, jname):
    try:
        logpath = configurations.sqplogdir \
                  + str(jrunid) + '_' \
                  + str(jname) + '_' \
                  + str(date.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '') \
                  + configurations.sqplogfileformat
        return logpath
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


def getcurrdatetime():
    try:
        currval = str(date.now()).replace('-', '').replace(' ', '').replace(':', '').replace('.', '')
        return currval
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


def rununixcommand(cmd, logfile=None):
    try:
        cmdlist = []
        for a in cmd.split(' '):
            cmdlist.append(a)

        # if logfile name has been passed as parameter
        if logfile != None:
            with open(logfile, 'w') as file:
                proc = subprocess.Popen(cmd, shell=True, stdout=file, stderr=file)
                proc.communicate()
                return proc.returncode
        else:
            proc = subprocess.Popen(cmdlist, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            sout, serr = proc.communicate()
            return sout, serr, proc.returncode
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


def decryptpassword(encryptedval):
    try:
        logging.info('Encrypted value received is %s', encryptedval)
        decoded_val = base64.b64decode(encryptedval)
        obj = ARC4.new(configurations.decryptionkey)
        decryptedpassword = obj.decrypt(decoded_val)
        return decryptedpassword
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


def getsqoopjobcrlogpath(jrunid, jname):
    try:
        logpath = configurations.sqplogdir \
                  + str(jrunid) + '_' \
                  + str(jname) + '_' \
                  + str(date.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '') \
                  + '_jobcreation' \
                  + configurations.sqplogfileformat
        return logpath
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


def avroexeclogpath(jrunid, jname):
    try:
        logpath = configurations.sqplogdir \
                  + str(jrunid) + '_' \
                  + str(jname) + '_' \
                  + str(date.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '') \
                  + '_avrotablecreation' \
                  + configurations.sqplogfileformat
        return logpath
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))
