 import socket

# Creating a socket.
inp = socket.socket()

# Socket Created
port = 1000
inp.bind(('', port))
inp.listen(5)

while True:
    client, address = inp.accept()
    print(address, 'connected')
    client.send( b'Oie chuutiya Anmol.')

client.close()
