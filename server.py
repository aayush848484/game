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
    # Run the game on the server.


    """
    new_game = Game('Aayush', 'Anmol')
    curr_player = new_game.decide_first_player()
    while not new_game.is_game_over():
        curr_player = new_game.next_player(curr_player)
        new_game.show_board()
        while True:
            index = int(input("{} Enter the index (1-9)".format(curr_player)))
            temp = new_game.validate_and_make_move(curr_player, index-1)
            if temp:
                break
    new_game.show_board()
    if new_game.is_draw:
        print('This is a draw.')
    else:
        print('Congratulations', curr_player)
    """
    while True:
        send_data = input("Enter a text that you want to send: ")
        client.send(send_data.encode())
        data = client.recv(1024)
        print(data)

client.close()
