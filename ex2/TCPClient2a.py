
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '10.0.0.7'
dest_port = 12345
s.connect((dest_ip,dest_port))

# The message we send is a string of 15,000 A's
msg = "A" * 15000

s.send(msg)
data = s.recv(4096) # Receives the response from the server
print "Server sent:", data


s.close()

