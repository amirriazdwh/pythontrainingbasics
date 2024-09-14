class MetaDBConfig:
    def __init__(self, server, name, schema, driver, username, password):
        self.server = server
        self.name = name
        self.schema = schema
        self.driver = driver
        self.username = username
        self.password = password


class LoggingConfig:
    def __init__(self, dir, file_name_init, file_format):
        self.dir = dir
        self.file_name_init = file_name_init
        self.file_format = file_format


class SMTPConfig:
    def __init__(self, server, from_mail, to_mail, cc_mail):
        self.server = server
        self.from_mail = from_mail
        self.to_mail = to_mail
        self.cc_mail = cc_mail


class SqoopConfig:
    def __init__(self, log_dir, log_file_format, output_dir, reccntfind_string, inc_job_name_prefix, hive_additional_col_name,
                 mapper_memory, java_heap, oraoop_timestamp, map_uber_task, runtime_col_mapping, inc_zero_rec_string):
        self.log_dir = log_dir
        self.log_file_format = log_file_format
        self.output_dir = output_dir
        self.reccntfind_string = reccntfind_string
        self.inc_job_name_prefix = inc_job_name_prefix
        self.hive_additional_col_name = hive_additional_col_name
        self.mapper_memory = mapper_memory
        self.java_heap = java_heap
        self.oraoop_timestamp = oraoop_timestamp
        self.map_uber_task = map_uber_task
        self.runtime_col_mapping = runtime_col_mapping
        self.inc_zero_rec_string = inc_zero_rec_string


class TempDirectoryConfig:
    def __init__(self, hdfs_target_dir, tmp_dir, excel_tmp_dir, zip_tmp_dir, zip_tmp_dir_accs_rights):
        self.hdfs_target_dir = hdfs_target_dir
        self.tmp_dir = tmp_dir
        self.excel_tmp_dir = excel_tmp_dir
        self.zip_tmp_dir = zip_tmp_dir
        self.zip_tmp_dir_accs_rights = zip_tmp_dir_accs_rights


class EncryptionConfig:
    def __init__(self, decryption_key):
        self.decryption_key = decryption_key


class StatusConfig:
    def __init__(self, running_status, success_status, fail_status):
        self.running_status = running_status
        self.success_status = success_status
        self.fail_status = fail_status


class Configurations:
    def __init__(self):
        # Metadata DB Configuration
        self.metadb = MetaDBConfig(
            server='192,168,56,102',
            name='HADOOP_REPO',
            schema='DLINGESTIONUAT',
            driver='ODBC Driver 17 for SQL Server',
            username='hadoop',
            password='hadoop'
        )

        # Logging Configuration
        self.logging = LoggingConfig(
            dir='/home/hdpadmin/DataLakeIngestionUAT/batchlogs/',
            file_name_init='batchrunlog_batchid_',
            file_format='.txt'
        )

        # SMTP Configuration
        self.smtp = SMTPConfig(
            server='172.24.81.89',
            from_mail='amir.riaz@test.com',
            to_mail=['xyz@test.com', 'abc@test.com'],
            cc_mail=['cdf@test.com', 'abc@test1.com']
        )

        # Sqoop Configuration
        self.sqoop = SqoopConfig(
            log_dir='/home/hdpadmin/DataLakeIngestionUAT/sqooplogs/',
            log_file_format='.log',
            output_dir='/home/hdpadmin/DataLakeIngestionUAT/sqoopTables/OUTPUT/',
            reccntfind_string='INFO mapreduce.ImportJobBase: Retrieved',
            inc_job_name_prefix='dl_',
            hive_additional_col_name='RUN_DATE_TIME',
            mapper_memory=8096,
            java_heap='Xmx8096m',
            oraoop_timestamp='false',
            map_uber_task='true',
            runtime_col_mapping='RUN_DATE_TIME=String',
            inc_zero_rec_string='INFO tool.ImportTool: No new rows detected since last import'
        )

        # Temp Directory Configuration
        self.temp_dir = TempDirectoryConfig(
            hdfs_target_dir='/home/hdpadmin/DataLakeIngestionUAT/tmp/tmpsqoop',
            tmp_dir='/home/hdpadmin/DataLakeIngestionUAT/tmp/',
            excel_tmp_dir='/home/hdpadmin/DataLakeIngestionUAT/tmp/tmpexcel/',
            zip_tmp_dir='/home/hdpadmin/DataLakeIngestionUAT/tmp/tmpzip/',
            zip_tmp_dir_accs_rights=0o777
        )

        # Encryption Configuration
        self.encryption = EncryptionConfig(decryption_key='hkjhkhkl')

        # Status Values
        self.status = StatusConfig(
            running_status='INPROGRESS',
            success_status='SUCCESS',
            fail_status='FAILED'
        )


# Example usage:
config = Configurations()

# Accessing metadata configurations
print(config.metadb.server)
print(config.logging.dir)
print(config.smtp.to_mail)
