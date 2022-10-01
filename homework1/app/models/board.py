import typing


class Board:
    CELLS_DEFAULT_VALUE = [['.'] * 3 for _ in range(3)]

    def __init__(self, cells: typing.Optional[list]):
        self.cells = cells if cells is not None else self.CELLS_DEFAULT_VALUE
        self.size = len(self.cells)

    def show(self):
        for i in self.cells:
            print(' | '.join(i))
