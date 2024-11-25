import os
import sys
import subprocess

subprocess.run(['git', 'fetch'], capture_output=True)
subprocess.run(['git', 'reset', '--hard', 'origin/main'], capture_output=True)

# os.execv(sys.executable, [sys.executable] + sys.argv)

# print('Hello (')
from core import ENV
print(ENV)
