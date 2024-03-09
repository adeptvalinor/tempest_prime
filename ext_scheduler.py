import os
import django
import subprocess

def ping_server(hostname):
    response = subprocess.run(['ping', '-W', '2', '-c', '1', hostname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Now you can import your models and work with them
from apps.home.models import Server

servers = Server.objects.all()

for server in servers:
    print (server.ip)
    if ping_server(server.ip):
        print ("Online")
    else:
        print ("Offline")
