from scapy.all import *

def spam_router():
    # router_mac = 
    # TODO use ARP and grep to get the router's address
    e = Ether(router_mac)
    t = TCP(flags = 'S')
    for i in range(10):
        send(e / IP() / t)

def main():
    spam_router()

if __name__ == "__main__":
    main()
