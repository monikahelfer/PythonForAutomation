# Example1: Create a script that executes example.py 5 times

# Import the library that allows python script to interact with the command line,
# which basically means that it executes a command line command
# The library offers many functions, we'll be using the check_call function
import subprocess

# Iterate to repeat the process 5 times
for i in range(0,5):
    # Execute example.py
    subprocess.check_call(['python3', 'example.py'])
# This script should take the script from the example.py file and call it 5 times