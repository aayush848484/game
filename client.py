import socket
server = socket.socket()

port = 1000

server.connect(('127.0.0.1', port))

print(server.recv(1024))
server.close()