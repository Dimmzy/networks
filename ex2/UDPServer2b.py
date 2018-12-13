from socket import socket, AF_INET, SOCK_DGRAM
 
s = socket(AF_INET,SOCK_DGRAM)
source_ip = '0.0.0.0'
source_port = 12345
s.bind((source_ip,source_port))
astr = ''
data,sender_info = s.recvfrom(1024)
data,sender_info = s.recvfrom(1024)
# Keeps receiving packets until we got 20 A's in our string (not inc first 2)
while len(astr) < 20:
    data, sender_info = s.recvfrom(1024)
    print 'Received: ', data
    if (data == 'A' or data == 'AA'):
        astr += data
    s.sendto('B', sender_info)

s.close()