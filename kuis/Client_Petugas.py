import socket
import select
import pickle

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(("127.0.0.1", 333))

tcp_sock.listen(100)

list_monitor = [tcp_sock]

while True :
    inputrdy, outputrdy, errorrdy, = select.select(list_monitor, [], [])

    for conn in inputrdy:
        if conn == tcp_sock:
            conn, client_addr = tcp_sock.accept()

            list_monitor.append(conn)
        else :
            try :
                data = conn.recv(100)

                data = raw_input(pickle.loads(data))

                print(data)

                data = pickle.dumps(data)
                conn.send(data)

                #conn.close()
            except(socket.error):
                conn.close
                list_monitor.remove(conn)
                print("Koneksi dimatikan")