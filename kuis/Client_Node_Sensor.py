import socket
import random
import pickle

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect(("127.0.0.1", 6667))



suhu = str(random.randint(25,50))
kelembapan = str(random.randint(60,90))
data = [suhu, kelembapan]
packet = pickle.dumps(data)

tcp_sock.send(packet)
data = tcp_sock.recv(100)
data = raw_input( pickle.loads(data))

print(data)


#tcp_sock.close()



