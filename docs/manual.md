# Netprowler


## How to use

This program's purpose is to allow for simple, small scale testing of your LAN.

### SYN flood on LAN computer (address resolved using ARP)

### What does it do?
1. Display contents of ARP cache

2. Read MAC and IP addresses from ARP cache

3. Generate network packets to perform a SYN flood
    * spoof MAC address with address of other computers, if possible
    * target every destination port
    * continuously send packets until `KeyboardInterrupt`
    
1. In the console, type in `sh get_macs.sh`
2. Type in `python3 dos.py`
  * It reads from the list of MAC and IP addresses and generates a [SYN flood](https://en.wikipedia.org/wiki/SYN_flood)
