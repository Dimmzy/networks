# Basic UDP server, expects datagrams

from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET,SOCK_DGRAM)
source_ip = '0.0.0.0'
source_port = 12345
s.bind((source_ip,source_port))
 
 
data,sender_info = s.recvfrom(20000)
print "Message: ", data
s.sendto("B", sender_info)
s.close()