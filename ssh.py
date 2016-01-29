import paramiko  # import the library

client = paramiko.SSHClient()  # open client SSH
client.set_missing_host_key(paramiko.AutoAddPolicy())
client.connect(username='username', password='password',
               port=port1, hostname='hostname')  # connect to the server
sftp = client.open_sftp()  # open an sftp connection
sftp.listdir()  # list the directories
