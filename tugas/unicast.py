import socket
import datetime
import time

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udp_socket.bind( ("0.0.0.0", 6666) )

packet, sender_addr = udp_socket.recvfrom(100)

data = packet.decode('ascii')

print(data)
#print(sender_addr)


date = str(datetime.datetime.now())
    
packet = "Sekarang "+ date

udp_socket.sendto(packet.encode('ascii'), sender_addr)

