import socket
from fungsi import recv_termination, send_termination

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(('', 6667))

tcp_sock.listen(100)

while True :
    conn, client_addr = tcp_sock.accept()

    data = recv_termination(conn)

    #data = data.decode('ascii')
    data = "OK" + data

    send_termination(conn, data)

    #conn.close()