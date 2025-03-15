import os
import subprocess
import sys

os.chdir('src')

python_executable = 'python'
if sys.platform == 'win32':
    python_executable = 'py'
elif sys.platform == 'linux' or sys.platform == 'darwin':
    python_executable = 'python3'

subprocess.run([python_executable, 'main.py'])

