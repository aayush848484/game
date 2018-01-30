player1_sign = 'O'
player2_sign = 'X'
is_draw = False


def initialize_board():
    return [[' ' for x in range(3)] for x in range(3)]


def show_board(game_board):
    for row in range(3):
        for column in range(3):
            print(' | {0} | '.format(game_board[row][column]), end=' ')
        print()


def next_player(current_player, player1, player2):
    return player2 if current_player == player1 else player1


def is_game_over(game_board, count):
    for counter in range(3):
        if game_board[counter][0] == game_board[counter][1] == game_board[counter][2] != ' ':
            return True
        if game_board[0][counter] == game_board[1][counter] == game_board[2][counter] != ' ':
            return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != ' ':
        return True
    elif game_board[0][2] == game_board[1][1] == game_board[2][0] != ' ':
        return True
    elif count == 9:
        global is_draw
        is_draw = True
        return True
    else:
        return False


def validate_and_make_move(game_board, current_player, player1):
    # Here normal index is converted to 2D index using the formula [input_index // 3][input_index - 3*(input_index//3)]
    while True:
        try:
            input_index = int(input('Enter the index in range(1-9): ').strip()) - 1
        except ValueError:
            print('Invalid Input. Please input a number.')
        if 8 >= input_index >= 0 and game_board[input_index // 3][input_index - 3 * (input_index // 3)] == ' ':
            break
        print('Enter a valid input index.')
    game_board[input_index // 3][input_index - 3 * (input_index // 3)] = player1_sign if current_player == player1 else player2_sign


def tic_tac_toe():
    import random
    play_again = 'y'
    while play_again == 'y':
        game_board = initialize_board()
        player1 = input('Enter the name of player1: ').strip()
        player2 = input('Enter the name of player 2: ').strip()
        current_player = player1 if random.randint(1, 2) == 1 else player2
        # Count variable to check if game is draw when 9 moves have been made. 
        count = 0
        while not is_game_over(game_board, count):
            count += 1
            current_player = next_player(current_player, player1, player2)
            show_board(game_board)
            print('Move for ', current_player, player1_sign if current_player == player1 else player2_sign)
            # Validates the move and if valid, makes changes to the game board.
            validate_and_make_move(game_board, current_player, player1)
        if is_draw:
            print("It's a draw.")
        else:
            print('Congratulations! {0}'.format(current_player))
        play_again = input("Play again(y/n): ").strip()
    print('Thank you! I hope that you enjoyed your game. ')


tic_tac_toe()

