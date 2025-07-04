import socket
import threading

ip = '0.0.0.0'
port=9999

def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(6)
    print(f'[*] Listening on {ip}:{port}')

    while True: #Accepts connection in loop
        client,address=server.accept() #accept() waits for a client to connect.
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler=threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

# def handle_client(client_socket):
#     with client_socket as sock:
#         request=sock.recv(1024)
#         print(f"[*] Received: {request.decode('UTF-8')}")
#         sock.send(b'ACK')

def handle_client(client_socket):
    with client_socket as sock:
        while True:
            try:
                request = sock.recv(1024)
                if not request:
                    break  # Client closed connection
                print(f"[*] Received: {request.decode('UTF-8')}")
                sock.send(b'ACK')
            except Exception as e:
                print(f"[!] Error: {e}")
                break

if __name__ == '__main__':
    main()



'--------------------------------------------------------------------------------------'
"Theory"
'''The listening socket stays open, continuing to accept new connections.
Each new connection gets its own socket so that:

Data doesn't get mixed up between clients.
You can spawn a new thread for each one and handle them independently.'''

# The first socket (server) is for listening only.

# Every time accept() runs, a new socket is created for communication with one client.

# This design allows the server to:

# Handle multiple clients at once

# Avoid conflicts in communication

# Scale better