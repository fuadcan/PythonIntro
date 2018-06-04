import paramiko,os,time
ssh = paramiko.SSHClient()
passwd = input('passwd: ')

ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
ssh.connect('192.168.1.16', username='pi', password=passwd)


command = '''
cd Documents/PythonIntro/playlist
python soundsense.py
'''
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)

# print('in:', ssh_stdin)
print('out:', ssh_stdout.read())

while True:
    time.sleep(1)
