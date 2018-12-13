
from socket import socket, AF_INET, SOCK_DGRAM
import time

def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    dest_ip = "10.0.0.7"
    dest_port = 12345
    msg = 'A'
    # Sends two A's without waiting for a response
    sock.sendto(msg, (dest_ip, dest_port))
    sock.sendto(msg, (dest_ip, dest_port))
    # Every two seconds ,sends two more A's and prints the response
    for x in range (11):
    	time.sleep(2)
    	sock.sendto(msg, (dest_ip, dest_port))
    	sock.sendto(msg, (dest_ip, dest_port))
    	data, sender_info = sock.recvfrom(2048)
    	print "Server sent: ", data
    sock.close()

if __name__ == "__main__":
    main()
