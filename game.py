
class Game:
        pl_s = 'X'
        pl_f = 'O'

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = ['0' for x in range(9)]

    def make_move(self, player, index):
        if self.


    def is_valid_move(self, index):
        pass

    def is_game_over(self):
        pass
    
    def next_player(self, player):
        pass
    
    def winner(self, player):
        pass

    