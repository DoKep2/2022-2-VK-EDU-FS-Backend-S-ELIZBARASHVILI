import typing

from homework1.app.exceptions.invalid_move import InvalidMoveException


class Board:
    CELLS_DEFAULT_VALUE = [['.'] * 3 for _ in range(3)]
    CELLS_AVAILABLE_DEFAULT_COUNT = 9

    def __init__(self, cells: typing.Optional[list]):
        self.cells = cells if cells is not None else self.CELLS_DEFAULT_VALUE
        self.size = len(self.cells)
        self.available_cells = (sum(i == '.' for j in cells for i in j) if cells is not None
                                else self.CELLS_DEFAULT_VALUE)

    def show(self):
        for i in self.cells:
            print(' | '.join(i))

    def validate_input(self, vertically, horizontally):
        if (not 0 < horizontally <= self.size or not 0 < vertically <= self.size
                or self.cells[vertically - 1][horizontally - 1] != '.'):
            raise InvalidMoveException("Invalid move")

    def check_horizontally(self, horizontally, turn):
        for i in range(self.size):
            if self.cells[i][horizontally] != turn:
                return False
        return True

    def check_vertically(self, vertically, turn):
        for i in range(self.size):
            if self.cells[vertically][i] != turn:
                return False
        return True

    def check_diagonally(self, turn):
        for i in range(self.size):
            if self.cells[i][i] != turn:
                return False
        return True

    def check_rev_diagonally(self, turn):
        for i in range(self.size):
            if self.cells[self.size - 1 - i][i] != turn:
                return False
        return True
