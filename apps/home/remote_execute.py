import subprocess
import os

# Get content from DB
key_content = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBrz7F9QJHsyq0U8eH/VVTPp984WsWFJ3INGHbLtpagCAAAAJhT1QnaU9UJ
2gAAAAtzc2gtZWQyNTUxOQAAACBrz7F9QJHsyq0U8eH/VVTPp984WsWFJ3INGHbLtpagCA
AAAED7AFwIlE+CVy/J0Fx5P7rLnhaKI6ncGqxIoZHLwbRghmvPsX1AkezKrRTx4f9VVM+n
3zhaxYUncg0Ydsu2lqAIAAAAEXVidW50dUByZXktODM0Njk5AQIDBA==
-----END OPENSSH PRIVATE KEY-----
"""

temp_folder = "/home/ubuntu/django-adminkit/"
key = "temp_key"

def opener(path, flags):
    return os.open(path, flags, 0o600)


with open(temp_folder+key, 'w', opener=opener) as fh:
    fh.write(key_content)

commands = ["ssh", "-i", temp_folder+key, "-oStrictHostKeyChecking=no", "-oUserKnownHostsFile=/dev/  null", "ubuntu@127.0.0.1", "ip addr"]

results = subprocess.run(commands, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#print (results.stdout)
print (results.stdout.decode('ascii'))

os.remove(temp_folder + key)
