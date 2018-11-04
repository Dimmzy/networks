import sys
from socket import socket, AF_INET, SOCK_DGRAM


# Need to add master server IP Address Validation
ipList = open(str(sys.argv[4]), 'r+')
ip_dict = {}
for line in ipList:
    line = line.strip()
    (key, val) = line.rsplit(',')
    ip_dict[key] = val
source_ip = '0.0.0.0'
source_port = int(sys.argv[1])
parentIP = str(sys.argv[2])
parentPort = int(sys.argv[3])
s = socket(AF_INET, SOCK_DGRAM)
s.bind((source_ip,source_port))
while True:
    data, sender_info = s.recvfrom(2048)
    found = 0
    for address in ip_dict:
        if data == address:
            found = 1
            s.sendto(ip_dict[address], sender_info)
            break
    if not found:
        clientSender = sender_info
        s.sendto(data,(parentIP,parentPort))
        data, sender_info = s.recvfrom(2048)
        s.sendto(data, clientSender)
