import sys
from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM) 
dest_ip = str(sys.argv[1]) 
dest_port = int(sys.argv[2])
msg = raw_input("Find IP of: ") 
while not msg == 'quit': 
    s.sendto(msg,(dest_ip,dest_port)) 
    data, sender_info = s.recvfrom(2048)
    print "IP Address: ", data
    msg = raw_input("Find IP of: ")
s.close()

