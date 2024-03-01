import subprocess
import sys
from django.core.management import call_command

subprocess.check_call([sys.executable, "-m", "pip", "install", 'r', 'requirements.txt'])
subprocess.check_call([sys.executable, 'manage.py', 'migrate'])
subprocess.check_call([sys.executable, 'manage.py', 'collectstatic'])