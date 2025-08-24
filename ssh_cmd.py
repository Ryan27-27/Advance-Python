import paramiko
import getpass

def ssh_command(ip,port,user,passwd,cmd):
   client=paramiko.SSHClient()
   client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   client.connect(ip,port=port,username=user,password=passwd)
   _, stdout, stderr=client.exec_command(cmd) # NON-INTERACTIVE only one command
   output=stdout.readlines() + stderr.readlines()
   if output:
      print("-----Output-----")
      print(f'Welcome User {getpass.getuser()}')
      for line in output:
         print(line.strip())

if __name__ == "__main__":
   
   user=input('Username: ') or 'bandit0'
   password=getpass.getpass("Password: ")
   ip=input('Enter server IP: ') or 'bandit.labs.overthewire.org'
   port = input('Enter port or <CR>: ') or 2220
   cmd=input('Enter command or <CR>: ') or 'id'
   ssh_command(ip,port,user,password,cmd)




#Theory about paramiko:

'''Paramiko is a pure-Python implementation of the SSHv2 protocol, providing both client and server functionality for secure communication.
   It enables Python applications to interact with remote devices over SSH, facilitating tasks such as running remote shell commands and transferring files. '''

'''Use cases for Paramiko:
1.Automating system administration tasks: Executing commands on remote servers, managing services, and monitoring system resources.
2.Secure file transfers: Uploading and downloading files to/from remote machines using SFTP.
3.Building custom SSH-enabled applications: Developing Python applications that require secure communication with remote systems.
4.Implementing SSH tunneling: Creating secure tunnels for forwarding network traffic.'''

#Theory about getpass:
'''
1.In Python, getpass is a module that allows you to safely handle password input (or other sensitive data) from users without
  showing it on the screen (i.e., the input is hidden).
2.Normally, when you use input(), whatever the user types is visible.
  With getpass.getpass(), the characters typed are not echoed to the terminal, keeping the input secret.
3.Hiding input (passwords, API keys, secrets) → getpass()
  Getting the current system username safely → getuser()    
'''