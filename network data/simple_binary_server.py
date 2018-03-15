import socket
import struct

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(('', 6667))

tcp_sock.listen(100)

while True :
    conn, client_addr = tcp_sock.accept()

    data = conn.recv(4)

    data = struct.unpack("<I", data)[0]
    data = data + 200
    data = "OK " + str(data)
    print data

    conn.send(data.encode('ascii'))

    #conn.close()