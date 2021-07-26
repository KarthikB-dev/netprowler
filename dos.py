from scapy.all import *
import argparse

# Generates packets to overwhelm your router
def is_ipv6(address):
    return address.index(":") != -1


def spam_router(router_mac, router_ip):
    # router_mac =
    # TODO use ARP and grep to get the router's address
    e = Ether(router_mac)
    t = TCP(flags="S")
    if is_ipv6(router_ip):
        i = IPv6()
    else:
        i = IP()
    i.dst = router_ip
    for i in range(10):
        send(e / IP() / t)

def extract_mac():
    with open('arp_query.txt') as fin:
    # TODO read from arp_query.txt

def main():
    spam_router()

if __name__ == "__main__":
    main()
