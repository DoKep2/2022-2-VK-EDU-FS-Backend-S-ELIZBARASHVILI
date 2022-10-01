from homework1.app.exceptions.invalid_move import InvalidMoveException
from homework1.app.models.board import Board


class TicTacToeGame:
    CONGRATULATION_WIN = "Winner winner chicken dinner:"
    CONGRATULATION_DRAW = "Oops, a draw was happen"
    MOVE_REQUEST = "Enter vertical and horizontal"

    def __init__(self, board: Board):
        self.board = board

    def congratulation(self, name):
        print(f"{self.CONGRATULATION_WIN} {name}")

    def show_board(self):
        self.board.show()

    def validate_input(self, vertically, horizontally):
        if (horizontally <= 0 or horizontally > self.board.size or vertically <= 0
                or vertically > self.board.size or self.board.cells[vertically - 1][horizontally - 1] != '.'):
            raise InvalidMoveException("Invalid move")

    def move(self, turn):
        print(self.MOVE_REQUEST)
        try:
            vertically, horizontally = map(int, input().split())
        except ValueError:
            raise InvalidMoveException("Move should be two integers")
        self.validate_input(vertically, horizontally)
        self.board.cells[vertically - 1][horizontally - 1] = turn

    def start(self, turn='x'):
        while not self.check_draw():
            self.show_board()
            self.move(turn)
            if self.check_winner(turn):
                self.show_board()
                self.congratulation(turn)
                return
            turn = '0' if turn == 'x' else 'x'
        print(self.CONGRATULATION_DRAW)

    def check_horizontally(self, horizontally, turn):
        for i in range(self.board.size):
            if self.board.cells[i][horizontally] != turn:
                return False
        return True

    def check_winner(self, turn):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if (self.check_horizontally(j, turn) or self.check_vertically(i, turn) or
                        self.check_diagonally(turn) or self.check_rev_diagonally(turn)):
                    return True
        return False

    def check_draw(self):
        for i in self.board.cells:
            for j in i:
                if j == '.':
                    return False
        return True

    def check_vertically(self, vertically, turn):
        for i in range(self.board.size):
            if self.board.cells[vertically][i] != turn:
                return False
        return True

    def check_diagonally(self, turn):
        for i in range(self.board.size):
            if self.board.cells[i][i] != turn:
                return False
        return True

    def check_rev_diagonally(self, turn):
        for i in range(self.board.size):
            if self.board.cells[self.board.size - 1 - i][i] != turn:
                return False
        return True


if __name__ == '__main__':
    game = TicTacToeGame(Board(None))
    game.start()
