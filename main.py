import subprocess

subprocess.run(['git', 'fetch'], capture_output=True)
subprocess.run(['git', 'reset', '--hard', 'origin/main'], capture_output=True)


print('Hello )')
