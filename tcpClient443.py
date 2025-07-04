import socket
import ssl

target= input('Enter the ip address or domain name of the target: ')
port=int(input("Enter the port number of the target: "))

# create a socket object
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# wrap the socket with ssl
context=ssl.create_default_context()
secure_client=context.wrap_socket(client, server_hostname=target)

# connect to the server
secure_client.connect_ex((target,port))

# send a valid data
secure_client.sendall(f'GET / HTTP/1.1\r\nHOST:{target}\r\n\r\nConnection: close\r\n\r\n'.encode())

# Receive and print response
response=b''
while True:
    data=secure_client.recv(4096)
    if not data:
        break
    response+=data
print(response.decode(errors='ignore'))

secure_client.close()
