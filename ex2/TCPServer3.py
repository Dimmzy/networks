# TCP Server

import socket, threading, re, os.path

# Setting up the Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip,server_port))
server.listen(0)
 
# Regex patterns we'll use
pattern = re.compile("GET\s([^\s]+)\sHTTP/1.1") # Proper request regex
jpgPattern = re.compile("([^\s]+)\.jpg") # JPG file regex
 
 
while True:
    client_socket, client_address = server.accept()
    print 'Connection from:', client_address
    data = client_socket.recv(1024)
    if pattern.match(data): # Checks if the user sent a valid request
        split = data.split(" ")
        if split[1] == "/": # Checks if the file is simply / (Opens index)
            print("Index requested")
            client_socket.send("HTTP/1.1 200 OK\nConnection: close\r\n\r\n")
            f = open("files/index.html", 'r')
            l = f.read(1024)
            while (l):
                client_socket.send(l)
                l = f.read(1024)
            f.close()
        elif jpgPattern.match(split[1]): # Check if the file is a JPG type
            print("JPG file requested: " + split[1])
            client_socket.send("HTTP/1.1 200 OK\nConnection: close\r\n\r\n")
            try: # Tries opening and sending the file, if file not found, returns 404
                with open("files" + split[1], 'rb') as f:
                    l = f.read(1024)
                    while (l):
                        client_socket.send(l)
                        l = f.read(1024)
                    f.close()  
            except IOError as e:
                client_socket.send("HTTP/1.1 404 Not Found\nConnection: close\r\n\r\n")
        elif split[1] == "/redirect": # Redirects if requested
            print("Redirect request")
            client_socket.send("HTTP/1.1 301 Moved Permanently\nConnection: close\nLocation: /result.html\r\n\r\n")
        else:
            print("Regular file requetssed: " + split[1])
            client_socket.send("HTTP/1.1 200 OK\nConnection: close \r\n\r\n")
            try: # Tries opening and sending the file, if file not found, returns 404
                with open("files" + split[1], 'r') as f:
                    l = f.read(1024)
                    while (l):
                        client_socket.send(l)
                        l = f.read(1024)
                    f.close()
            except IOError as e:
                client_socket.send("HTTP/1.1 404 Not Found\nConnection: close\r\n\r\n")
    client_socket.close()