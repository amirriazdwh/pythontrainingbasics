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


import subprocess

def run_command(command):
    try:
        # Execute the command
        result = subprocess.run(command, check=True, text=True, capture_output=True)

        # If the command succeeded, print the output
        print("Success:", result.stdout)
    except subprocess.CalledProcessError as e:
        # If the command failed, print the error message and exit code
        print("Error:", e.stderr)
        print("Exit code:", e.returncode)


# Example: Run a successful command
run_command(["ls", "/path/to/directory"])

# Example: Run a command that will fail
run_command(["invalid_command"])



