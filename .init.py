import subprocess

subprocess.run(f'pip unistall python-ffmpeg', shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
subprocess.run(f'pip install python-ffmpeg', shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)