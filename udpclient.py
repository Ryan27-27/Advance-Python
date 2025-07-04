# import socket

# target=input('Enter the target ip address or domain name: ')
# port=int(input("Enter the target port: "))

# # create a socket client
# client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# connectionless as we don't need to connect 
# # send data 
# client.sendto(b"Hello world i just send a udp data",(target,port))

# # receive data
# # data,addr=client.recvfrom(4096)

# # print data
# # print(f"{data} : {addr}")
# client.close()

import socket

target = "172.17.251.224" # wsl ip address for udp connection
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello from UDP client", (target, port))
client.close()
