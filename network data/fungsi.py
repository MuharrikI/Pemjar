import struct

def send_termination(conn, data):
    term_char = "\r\n"

    data = data + term_char
    data = data.encode('ascii')

    conn.send(data)



def recv_termination(conn):
    data = ''

    while True:
    
        buffer = conn.recv(20)
        buffer = buffer.decode('ascii')
        if "\r\n" in buffer:
            buffer = buffer.replace("\r\n", "")
            data = data + buffer
            return data

        data = data + buffer



def send_size(conn, data):
    size = len(data)

    size = struct.pack("<I", size)

    data = data.encode('ascii')

    data = size + data

    conn.send(data)


def recv_size(conn):
    size = conn.recv(4)
    size  = struct.unpack("<I", size)[0]

    data = conn.recv(size)

    data = data.decode('ascii')

    return data