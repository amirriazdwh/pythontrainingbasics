import logging
import subprocess

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


# Function to run Hadoop command
def run_unix_cmd(args_list):
    """
    run linux commands
    """
    print('Running system command:{0}'.format('     '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output, s_err


# Create Sqoop Job
def sqoop_job():
    """
    Create Sqoop job
    """
    cmd = ['sqoop', 'import', '--connect', 'jdbc:oracle:thin:@//host:port/schema', '--username', 'user', '--password',
           'XX', '--query', '"query"', '-m', '1', '--target-dir', 'tgt_dir']
    print(cmd)
    (ret, out, err) = run_unix_cmd(cmd)
    print(ret, out, err)
    if ret == 0:
        logging.info('Success.')
    else:
        logging.info('Error.')


if __name__ == '__main__':
    sqoop_job()
