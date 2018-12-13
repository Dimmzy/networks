
import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '10.0.0.7'
dest_port = 12345
s.connect((dest_ip,dest_port))
# Sends two messages and not expect any response (as per the exercise)
msg = 'A'
s.send(msg)
s.send(msg)
# Sends the messages 10 more times, with 2 sec delay with each sending
for x in range(10):
    time.sleep(2)
    s.send(msg)
    s.send(msg)
    data = s.recv(4096)
    print "Server Sent:", data
data = s.recv(4096)
print "Server Sent:", data
s.close()
