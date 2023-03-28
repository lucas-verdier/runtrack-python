class Board:

    def __init__(self, i, j):
        self.board = [['O' for _ in range(j)] for _ in range(i)]
        self.row = i
        self.col = j

    def play(self, col, color):
        k = len(self.board) - 1
        while self.board[k][col - 1] != 'O':
            k -= 1
        self.board[k][col - 1] = color

    def print(self):
        for row in self.board:
            print(' | '.join(row))


game = Board(6, 8)
game.play(4, "R")
game.play(3, "J")
game.play(3, "J")
game.play(3, "R")
game.print()
