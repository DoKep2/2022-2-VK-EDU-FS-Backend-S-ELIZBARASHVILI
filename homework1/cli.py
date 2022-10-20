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

    def move(self, turn):
        print(self.MOVE_REQUEST)
        try:
            vertically, horizontally = map(int, input().split())
        except ValueError:
            raise InvalidMoveException("Move should be two integers")
        self.board.validate_input(vertically, horizontally)
        self.board.cells[vertically - 1][horizontally - 1] = turn

    def start(self, turn='x'):
        while self.board.available_cells:
            self.show_board()
            self.move(turn)
            if self.check_winner(turn):
                self.show_board()
                self.congratulation(turn)
                return
            turn = '0' if turn == 'x' else 'x'
        print(self.CONGRATULATION_DRAW)

    def check_winner(self, turn):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if (self.board.check_horizontally(j, turn) or self.board.check_vertically(i, turn) or
                        self.board.check_diagonally(turn) or self.board.check_rev_diagonally(turn)):
                    return True
        return False


if __name__ == '__main__':
    game = TicTacToeGame(Board(None))
    game.start()
