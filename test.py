import subprocess

search = subprocess.run('python3 parser.py', shell=True, capture_output=True)
print(search.stdout)
