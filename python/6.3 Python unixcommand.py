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

"""

"""

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

"""
Running Commands in Background and Checking Status
If you want to run commands in the background and check their status later, you can use subprocess.Popen:
"""
import subprocess
import time

def run_command_in_background(command):
    process = subprocess.Popen(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

# Example: Start a background command
process = run_command_in_background(["sleep", "5"])  # Simulating a long-running command

# Do other tasks while the command is running
print("Command is running in the background...")

# Wait for the process to complete
stdout, stderr = process.communicate()
exit_code = process.returncode

if exit_code == 0:
    print("Command succeeded:", stdout)
else:
    print("Command failed with exit code", exit_code)
    print("Error output:", stderr)

"""

"""



