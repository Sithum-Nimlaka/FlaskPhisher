import platform
import subprocess

def screenCleaner():
    if platform.system() == 'Windows':
        subprocess.call(['cls'], shell=True)

    elif platform.system() == 'Linux':
        subprocess.call(['clear'], shell=True)

    elif platform.system() == 'Darwin':
        subprocess.call(['clear'], shell=True)