import socket 
import datetime


##today = datetime.datetime.today()
##print(str(today))
##tomorrow = today + datetime.timedelta(days=1)
##yesterdey = today - datetime.timedelta(days=1)

udp_sock = socket.socket(socket.AF_INET, socket. SOCK_DGRAM)

udp_sock.bind(("127.0.0.1", 6666))


data, client_addr = udp_sock.recvfrom(100)

data = data.decode('ascii')

##data = "OK " + data

today = datetime.datetime.today()
if data == "today" :
    data = datetime.datetime.today()
elif data == "tomorrow" :
    data = today + datetime.timedelta(days=1)
elif data == "yesterday" :
    data = today - datetime.timedelta(days=1)
else:
    data = "error"

data = str(data)

udp_sock.sendto(data.encode('ascii'), client_addr)