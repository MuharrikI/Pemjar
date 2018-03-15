import socket
from fungsi import recv_size, send_size

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(('', 6667))

tcp_sock.listen(100)

while True :
    conn, client_addr = tcp_sock.accept()

    data = recv_size(conn)

    #data = data.decode('ascii')
    data = "OK" + data

    send_size(conn, data)

    #conn.close()