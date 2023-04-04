import paramiko

import time

ssh = paramiko.SSHClient()

hostname = '10.0.0.2'
port = '22'
username = 'root'
password = 'cjq20030308'
print("About to connect to the server: \n Host: " + hostname + "\n User: " + username)

pppoe_pw = str(input("Input PPPOE Password: "))
cmd = "./pppoe.sh "+ pppoe_pw

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
stdin, stdout, stderr = ssh.exec_command(cmd)
print("Connecting to " + hostname)

time.sleep(1)
print("Restarting network service...")

time.sleep(6)

ssh.close()