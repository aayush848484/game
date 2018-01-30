player1_sign = 'O'
player2_sign = 'X'
is_draw = False


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.is_draw = False
        self.count = 0

    def show_board(self):
        for row in range(3):
            for column in range(3):
                print(' | {0} | '.format(self.board[row][column]), end=' ')
            print()

    def next_player(self, current_player):
        return self.player2 if current_player == self.player1 else self.player1

    def is_game_over(self):
        for counter in range(3):
            if self.board[counter][0] == self.board[counter][1] == self.board[counter][2] != ' ':
                return True
            if self.board[0][counter] == self.board[1][counter] == self.board[2][counter] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        elif self.count == 9:
            self.is_draw = True
            return True
        else:
            return False

    def validate_and_make_move(self, current_player, input_index):
        if 8 >= input_index >= 0 and self.board[input_index // 3][input_index - 3 * (input_index // 3)] == ' ':
            self.board[input_index // 3][input_index - 3 * (input_index // 3)] = player1_sign \
                if current_player == self.player1 else player2_sign
            self.count += 1
            return True
        return False

    def decide_first_player(self):
        import random
        return self.player1 if random.randint(1,3) == 1 else self.player2


if __name__ == '__main__':
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



