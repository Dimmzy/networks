# TCP Client

import socket

# Creates a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '10.0.0.7'
dest_port = 12345
s.connect((dest_ip,dest_port))

msg = raw_input("Message to send:")

# Keeps sending messages through the socket until quit input received
while not msg == 'quit':
	s.send(msg)
	data = s.recv(4096) # Receives messages from server
	print "Server sent:", data
	msg = raw_input("Message to send:")

s.close()

