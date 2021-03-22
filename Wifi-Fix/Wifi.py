import socket

host = socket.gethostname()
port = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


test = "Test"
sock.bind((host, port))
sock.listen(5)
data = sock.recv(1024).decode(test)
while True:
    client, addr = sock.accept()
    print("Connected to", addr)
    sock.send(test.encode(), port)
print(data)