import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect(("127.0.0.1", 6667))

data = "Selamat Sore"

tcp_sock.send(data.encode('ascii'))

data = tcp_sock.recv(100)
data = data.encode('ascii')

print(data)

tcp_sock.close()