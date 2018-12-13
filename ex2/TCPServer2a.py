
import socket, threading
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip,server_port))
server.listen(0)
 
# Receives information in segments according to buffer size and appends them

def recvinfo(socket):
    BUFF_SIZE = 4096
    data = ''
    while True:
        dataseg = socket.recv(BUFF_SIZE)
        data += dataseg
        if len(dataseg) < BUFF_SIZE:
            break
    return data
 
while True:
    client_socket, client_address = server.accept()
    print 'Connection from:', client_address
    data = recvinfo(client_socket)
    print 'Received: ', data
    # Sends B after receiving everything
    client_socket.send("B")
    print 'Client disconnected'
    client_socket.close()
