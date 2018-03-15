import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

packet = "Siapa tahu sekarang tanggal dan jam berapa?"

broad_addr = ("192.168.88.255", 6666)
udp_socket.sendto(packet.encode('ascii'), broad_addr)




packet, sender_addr = udp_socket.recvfrom(100)

print(packet)
