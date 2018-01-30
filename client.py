import socket
server = socket.socket()

port = 1000

server.connect(('127.0.0.1', port))

while True:
    print(server.recv(1024))
    send_data = str(input('Enter the data that you want to send: '))
    server.sendall(send_data.encode())

server.close()