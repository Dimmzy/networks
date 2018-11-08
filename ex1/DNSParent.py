"""
A DNS Server program that receives address queries and returns their
corresponding IP addresses to the client.
A more complete documentation is in the DNSServer module
"""
import sys
from socket import socket, AF_INET, SOCK_DGRAM

def make_dict(ip_file):
    """
    Creates a dictionary from the given IP file for easier access
    and comparions.
    # Args:
    ip_file (file): A text file containing addresses and their IP's.
    # Returns:
    dictionary: A dictionary with the address as key and IP as value.
    Args:
        ip_file (TYPE): Description
    Returns:
        TYPE: Description
    """
    ip_dict = {}
    for line in ip_file:
        if line != '\n':
            line = line.strip()
            (key, val) = line.rsplit(',')
            ip_dict[key] = val
    return ip_dict

def main():
    """
    Starts up a socket and runs a DNS server that provides answers to IP
    address queries from clients.
    """
    ip_list = open(str(sys.argv[4]), 'r')
    ip_dict = make_dict(ip_list)
    source_ip = '0.0.0.0'
    source_port = int(sys.argv[1])
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((source_ip, source_port))
    while True:
        data, sender_info = sock.recvfrom(2048)
        for address in ip_dict:
            if data == address:
                sock.sendto(ip_dict[address], sender_info)
                break

if __name__ == "__main__":
    main()
