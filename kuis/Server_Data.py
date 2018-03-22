import socket
import select
import pickle

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock_petugas = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(("127.0.0.1", 6667))
tcp_sock_petugas.connect(("127.0.0.1", 333))

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

                data =raw_input(pickle.loads(data))
                if int(data[0]) > 40:
                    data.append(client_addr)
                    data.append("Warning")
                    packet = pickle.dumps(data)
                    tcp_sock_petugas.send(packet)
                packet = pickle.dumps(data)
                conn.send(packet)
                
                #conn.close()
            except(socket.error):
                conn.close
                list_monitor.remove(conn)
                print("Koneksi dimatikan")