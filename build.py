import subprocess
import sys


subprocess.check_call([sys.executable, "-m", "pip", "install", 'r', 'requirements.txt'])

subprocess.check_call([sys.executable, 'manage.py', 'migrate'])
# subprocess.check_call([sys.executable, 'manage.py', 'tailwind', 'build'])
subprocess.check_call([sys.executable, 'manage.py', 'collectstatic'])