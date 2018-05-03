from scapy.all import *
import sys

ip = "127.0.0.1"

for i in range(70, 90):
    paket_tcp = IP(dst=ip)/TCP(dport=1)
    answer = sr1(paket_tcp, retry=1, verbose=False)
    if answer is None:
        print("Port "+str(i)+"...Closed")
    else:
        if TCP in answer:
            print("Port "+str(i)+"...Open")
        else:
            print("Port "+str(i)+"...Closed")
    time.sleep(1)

#! /usr/bin/python

#import logging
#logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#from scapy.all import *

#dst_ip = "10.0.0.1"
#src_port = RandShort()
#dst_port = (1, 65356)

#tcp_connect_scan_resp = sr1(
    #IP(dst=dst_ip)/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=10)
#if(str(type(tcp_connect_scan_resp)) == "<type 'NoneType'>"):
#print "Closed"
#elif(tcp_connect_scan_resp.haslayer(TCP)):
#if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
#send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,
 #                                dport=dst_port, flags="AR"), timeout=10)
#print "Open"
#elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
#print "Closed" 
