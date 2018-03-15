import socket
from fungsi import recv_termination, send_termination

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect(("127.0.0.1", 6667))

data = "Selamat Sore \r\n"

send_termination(tcp_sock, data)

data = tcp_sock.recv(100)
data = recv_termination(tcp_sock)

print data

tcp_sock.close()