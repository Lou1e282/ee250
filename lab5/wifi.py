import subprocess
import re


output = subprocess.check_output("netsh wlan show interfaces", shell=True)

print(output) 