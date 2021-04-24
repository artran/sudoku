from itertools import repeat

from sudoku.cell_group import CellGroup


class Board:
    def __init__(self):
        self.cols = [CellGroup(repeat(0, 9)) for _ in range(9)]
        self.rows = [CellGroup(repeat(0, 9)) for _ in range(9)]
        self.boxes = [CellGroup(repeat(0, 9)) for _ in range(9)]

    def set_value_at(self, col: int, row: int, value: int) -> None:
        pass
