import socket
import subprocess

subprocess.call('cls',shell=True)
# subprocess.call('mkdir newdir',shell=True)

target=input("Enter the web domain or ip address: ")
port=int(input("Enter the port that you want to connect: "))

#create a socket object
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ip=socket.gethostbyname(target)

#connect the client
client.connect_ex((target,port))

# send some data
client.sendall(f'GET / HTTP/1.1\r\nHOST:{target}\r\n\r\n'.encode()) #Sends entire message reliably 
# client.sendall(b'Hello World i am using tcp client to connect localhost using netcat')
i=1
while i<5:
    client.sendall(f'Data is being sent continuosly {i}'.encode('utf-8'))
    
# encode() converts the string to bytes (since sendall() requires bytes).

# receive some data
    response=client.recv(4096)

# print response
    print(f'Received from server\n{response.decode(errors='ignore')}')
    i+=1

# close socket object
client.close()
  

"--------------------------------------------------------"
"Theory"
# "\r\n\r\n"
#    This means: "End of HTTP headers; no body will follow."
#    It tells the server: "That's it — I'm done sending the request."

'\r\n :This is a line break (carriage return + line feed), required by the HTTP spec.'
'You can pass a domain name (like google.com) directly to socket.connect() or connect_ex() — Python will automatically resolve it to an IP address using DNS'


