import os
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))  #By using this line, your code becomes "environment-aware"
hello_script = os.path.join(script_dir, "helloworld.py")

for a in range(5):
    subprocess.check_call([sys.executable, hello_script])