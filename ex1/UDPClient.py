"""
A UDP Client program. Sends a query to a DNS server with the input address
and receives the adderss's IP from the DNS server.
"""
import sys
from socket import socket, AF_INET, SOCK_DGRAM

def main():
    """
    Creates a socket and sends the user input to the server specified in the
    program arguments.
    If the message that was sent is quit, close the socket and finish.
    """
    sock = socket(AF_INET, SOCK_DGRAM)
    dest_ip = str(sys.argv[1])
    dest_port = int(sys.argv[2])
    msg = raw_input("Find IP of: ")
    while not msg == 'quit':
        sock.sendto(msg, (dest_ip, dest_port))
        data, _ = sock.recvfrom(2048) # _ for sender info since we dont use it
        print "IP Address: ", data
        msg = raw_input("Find IP of: ")
    sock.close()

if __name__ == "__main__":
    main()
