'''
Module Name : configurations.py
Created On : 10th Nov 2019
Created By : amir riaz
Purpose : This module is for specifying all the configurations values to be used in the package
'''

# Metadata db configurations
metadb_server = '192,168,56,102'  # (in case of IP and Port both, enter as IP,Port with no space)
metadb_name = 'HADOOP_REPO'
metadb_schema = 'dbo'
metadb_driver = 'ODBC Driver 17 for SQL Server'
metadb_username = 'hadoop'
metadb_password = 'hadoop'
metadb_schema = 'DLINGESTIONUAT'

# Logging configurations
logging_dir = '/home/hdpadmin/DataLakeIngestionUAT/batchlogs/'
logging_file_name_init = 'batchrunlog_batchid_'
logging_file_format = '.txt'

# SMTP configurations
smtp_server = '172.24.81.89'
from_mail = 'amir.riaz@test.com'
to_mail = ['xyz@test.com', 'abc@test.com']
cc_mail = ['cdf@test.com', 'abc@test1.com']

# Sqoop Configurations
sqplogdir = '/home/hdpadmin/DataLakeIngestionUAT/sqooplogs/'
sqplogfileformat = '.log'
sqpoutdir = '/home/hdpadmin/DataLakeIngestionUAT/sqoopTables/OUTPUT/'
reccntfindString = 'INFO mapreduce.ImportJobBase: Retrieved'
incjobnameprefix = 'dl_'
hiveadditionalcolname = 'RUN_DATE_TIME'
mappermemory = 8096
javaheap = 'Xmx8096m'
oraooptimestamp = 'false'
mapubertask = 'true'
runtimecolmapping = 'RUN_DATE_TIME=String'
inczerorecString = 'INFO tool.ImportTool: No new rows detected since last import'

# Temp Directory
hdfstargetDir = '/home/hdpadmin/DataLakeIngestionUAT/tmp/tmpsqoop'
tmpdir = '/home/hdpadmin/DataLakeIngestionUAT/tmp/'
exltmpdir = '/home/hdpadmin/DataLakeIngestionUAT/tmp/tmpexcel/'
ziptmpdir = '/home/hdpadmin/DataLakeIngestionUAT/tmp/tmpzip/'
ziptmpdiraccsrights = 0o777

# Encryption configurations
decryptionkey = 'hkjhkhkl'

# Status values for database tables
runningstatus = 'INPROGRESS'
successstatus = 'SUCCESS'
failstatus = 'FAILED'
