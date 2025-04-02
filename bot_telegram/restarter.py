from asyncio.subprocess import PIPE, STDOUT
import subprocess
from funcs import *

filepath="main.py"

try:
    while True:
        mainProcess=subprocess.Popen("python3 "+filepath, shell=True)
except KeyboardInterrupt:
    mainProcess.kill()
    