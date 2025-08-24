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

'''
When you run:
ssh user@ipaddress

Your SSH client checks the server's host key against the ~/.ssh/known_hosts file.
If this is the first time connecting, there's no record of the host key yet.

SSH then prompts you:

The authenticity of host 'ipaddress (x.x.x.x)' can't be established.
RSA key fingerprint is SHA256:abcdefg...
Are you sure you want to continue connecting (yes/no)?

If you type yes, the host key gets saved to ~/.ssh/known_hosts.
Next time you connect, SSH compares the server's key with the saved one.

If it matches→ connect.
If it doesn't ❌ → you get a WARNING: POSSIBLE DNS SPOOFING / MITM ATTACK.
This is how OpenSSH protects you.
'''

'''
Meaning of set_missing_host_key_policy
It tells Paramiko what to do if the server's host key is not in the known_hosts file.

paramiko.AutoAddPolicy() means:
“Automatically trust the host key and add it to the known hosts (without asking).”
So it's like saying “yes” automatically when SSH asks “Do you trust this server?”.

Security Note:
AutoAddPolicy is convenient for testing/learning (like your Bandit labs).
But in real secure environments, it's risky because it means you blindly trust any server you connect to.
Safer option: use RejectPolicy (default) or manually load known host keys.

'''

'''
SFTP and FTPS are different.
both are file transfer protocol and secured/encrypted.
one uses ssh connection for more robust and uses file management run inside ssh connection.
ftps used TLS/SSL certifications for encryption.

scp and sftp are different
SCP = quick & simple → "just copy this file."
SFTP = powerful & flexible → "manage files like FTP but securely

Paramiko = Python library for SSH2
   SSH remote login
   Run commands on remote machines
   Secure file transfer (SFTP)
   Port forwarding / tunneling
   Automating server management

for more details read :
https://chatgpt.com/share/68ab0481-4924-8012-b025-66d983951340
'''