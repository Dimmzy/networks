
# Basisc UDP Client, nothing much to add

from socket import socket, AF_INET, SOCK_DGRAM

def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    dest_ip = "10.0.0.7"
    dest_port = 12345
    # Sends a message of A 15000 times
    msg = 'A' * 15000
    sock.sendto(msg, (dest_ip, dest_port))
    data, sender_info = sock.recvfrom(2048)
    print "Server sent: ", data
    sock.close()

if __name__ == "__main__":
    main()
