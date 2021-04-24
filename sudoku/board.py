from pprint import pprint
from typing import TextIO

from sudoku.cell_group import CellGroup


class Board:
    def __init__(self):
        self.cols = [CellGroup() for _ in range(9)]
        self.rows = [CellGroup() for _ in range(9)]
        self.boxes = [CellGroup() for _ in range(9)]
        self.full_board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def __str__(self) -> str:
        return f'{self.cols}, {self.rows}, {self.boxes}'

    def set_value_at(self, col_idx: int, row_idx: int, value: int) -> bool:
        col = self.cols[col_idx - 1]
        row = self.rows[row_idx - 1]
        box = self.boxes[(col_idx - 1) // 3 + 3 * ((row_idx - 1) // 3)]

        if any(value in group for group in (col, row, box)):
            return False

        col.insert(value)
        row.insert(value)
        box.insert(value)
        self.full_board[row_idx - 1][col_idx - 1] = value

        return True

    def print(self, output_stream: TextIO = None) -> None:
        pprint(self.full_board, output_stream)
