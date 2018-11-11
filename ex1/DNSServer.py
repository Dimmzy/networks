"""
A DNS Server program that receives address queries and returns their
corresponding IP addresses to the client.
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
    address queries from clients, if no match is found in the provided ips.txt
    file, passes the query to it's parent server. (defined in main args)
    """
    ip_list = open(str(sys.argv[4]), 'r+')
    ip_dict = make_dict(ip_list) # We create a dictionary using make_dict func
    source_ip = '0.0.0.0' # Listens to all the network cards
    source_port = int(sys.argv[1])
    parent_ip = str(sys.argv[2])
    parent_port = int(sys.argv[3])
    sock = socket(AF_INET, SOCK_DGRAM) # Binds its IP and Port to a new socket
    sock.bind((source_ip, source_port))
    while True: # Runs the server indefinitly
        data, sender_info = sock.recvfrom(2048) # Recevies queries from clients
        found = 0 # flag used to check if the query was answered
        # We perform a loop that compares the address in question with all
        # addresses given in teh ips file, if a match is found, return the IP
        # to the client and finish.
        for address in ip_dict:
            if data == address:
                found = 1
                sock.sendto(ip_dict[address], sender_info)
                break
        # If the address is not found in the dictionary, query the parent DNS
        # server and return the answer to the client.
        if not found:
            data_address = data
            client_sender = sender_info
            sock.sendto(data, (parent_ip, parent_port))
            data, sender_info = sock.recvfrom(2048)
            sock.sendto(data, client_sender)
            # The program also "remembers" the address and IP given, and writes
            # it to the ips.txt file and the dictionary.
            ip_list.write(data_address + ',' + data + '\n')
            ip_list.flush()
            ip_dict[data_address] = data

if __name__ == "__main__":
    main()
