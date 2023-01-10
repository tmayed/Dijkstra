import subprocess
import sys

def pip_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

pip_install("pip")
pip_install("numpy")