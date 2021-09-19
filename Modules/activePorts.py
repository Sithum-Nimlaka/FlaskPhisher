import psutil
import re
import subprocess

def get_active_ports():
    process = subprocess.run(['netstat', '-n'], capture_output=True)
    report = process.stdout.decode().splitlines()
    ports = []
    for i in report[4:]:
        ports.append(re.split(':(?!.*:)', re.split('\s+', i)[2])[1])
    return ports

s = get_active_ports()
