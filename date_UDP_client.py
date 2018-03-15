import socket


udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


data = "yesterday"
server_addr = ("127.0.0.1", 6666)

udp_sock.sendto(data.encode('ascii'), server_addr)

data, addr = udp_sock.recvfrom(100)

print (data.encode("ascii"))