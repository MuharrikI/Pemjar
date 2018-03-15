import socket
import os

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(('', 6667))

tcp_sock.listen(100)


conn, client_addr = tcp_sock.accept()

data = conn.recv(100)

data = data.decode('ascii')
data = data.split()
file_name = data[1]

if data[0]=="new":
    file = open(data[1]+".txt", "w")
    teks = "New Command Executed Successfully"
    conn.send(teks.encode('ascii'))
    print teks
elif data[0]=="del":
    os.remove(file_name+".txt")
    teks = "Delete Command Executed Successfully"
    conn.send(teks.encode('ascii'))
    print teks
elif data[0]=="write":
    with open(file_name+".txt") as f:
        teks = f.readlines()
        conn.send(teks.encode('ascii'))
        teks = "Read Command Executed Successfully"
        print teks

#conn.close()