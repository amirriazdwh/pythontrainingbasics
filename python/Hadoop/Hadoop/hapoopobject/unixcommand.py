import subprocess

def run_unix_cmd(args_list, output_file='output.txt', error_file='error.txt'):
    """
    Run a Unix command and write output and error to files.
    """
    print('Running system command: {0}'.format(' '.join(args_list)))

    with open(output_file, 'w') as out, open(error_file, 'w') as err:
        proc = subprocess.Popen(args_list, stdout=out, stderr=err, universal_newlines=True)
        proc.communicate()

    return proc.returncode


