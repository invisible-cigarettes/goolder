import subprocess

subprocess.run(['git', 'reset', '--hard', 'origin/main'], capture_output=True)
subprocess.run(['git', 'pull'], capture_output=True)


print('Hello, world! )2')
