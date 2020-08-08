import socket


def send_socket(port, *args):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = port
    client.connect((host, port))
    index = 0
    client.send(str(args[index]).encode('utf-8'))


def receive_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.bind((host, port))
    s.listen(1)
    s1, address = s.accept()
    d = s1.recv(2000).decode('utf-8')
    return d
