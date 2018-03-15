import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect(("127.0.0.1", 6667))

a = """
    'file_name' without file extensions
    
    List: 
    -new 'file_name'
    -del 'file_name'
    -read 'file_name'
    """
print a
inputan = raw_input("Command: ")

data = inputan

tcp_sock.send(data.encode('ascii'))



data = tcp_sock.recv(1000)
data = data.decode('ascii')

print data
tcp_sock.close()