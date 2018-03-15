
import socket
from threading import Thread

def handle_thread(conn):
    while True :
        try :
            data = conn.recv(100)

            data = data.decode('ascii')
            data = "OK" + data

            conn.send(data.encode('ascii'))

        except(socket.error):
            conn.close()
            print("Koneksi ditutup client")
            break

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(('', 6667))

tcp_sock.listen(100)

while True :
    conn, client_addr = tcp_sock.accept()

    t = Thread(target=handle_thread, args=(conn,))
    t.start()