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

import subprocess

# Command to be executed
cmd = "ls -l /invalid/path"  # This will fail

# Open a file to capture output and errors
with open('output.txt', 'w') as file:
    proc = subprocess.Popen(cmd, shell=True, stdout=file, stderr=file)
    proc.communicate()  # Wait for the command to complete

# Return the exit code
return_code = proc.returncode

if return_code == 0:
    print("Command executed successfully.")
else:
    print(f"Command failed with exit code: {return_code}. Check output.txt for details.")

"""
To add exception handling to the run_command_in_background function, you can use a try and except block to catch 
potential exceptions that may arise during the command execution. In the case of subprocess.Popen(), you can handle 
exceptions such as FileNotFoundError (if the command is invalid) or subprocess.SubprocessError (for any issues related 
to the subprocess itself).

Here’s how you can modify your code to include exception handling:

Updated Code with Exception Handling

Explanation of the Changes
Exception Handling in run_command_in_background:

A try block is added around the subprocess.Popen() call to catch exceptions that might occur when starting the subprocess.
FileNotFoundError: This exception is caught if the command does not exist or is not found in the system’s PATH.
subprocess.SubprocessError: This is a base class for subprocess-related errors and can be caught to handle other 
subprocess-related issues.
Return Value Handling:

If an exception occurs and the command cannot be started, the function returns None. This helps to handle cases where
the command fails to start gracefully in the main part of the code.
Main Code Execution:

Before trying to wait for the process to complete, it checks if process is not None. If it is None, an 
error message is printed, indicating that the command could not be started.
Summary
With these changes, your code now has basic exception handling for starting the command in the background. 
This will ensure that any issues encountered while trying to initiate the subprocess are caught and reported without 
crashing the entire program
"""
import subprocess

def run_command_in_background(command):
    try:
        # Start the background process
        process = subprocess.Popen(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process
    except FileNotFoundError as e:
        print(f"Error: Command not found: {e}")
        return None
    except subprocess.SubprocessError as e:
        print(f"Error: A subprocess error occurred: {e}")
        return None

# Example: Start a background command
process = run_command_in_background(["sleep", "5"])  # Simulating a long-running command

if process is not None:
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
else:
    print("Failed to start the command.")



