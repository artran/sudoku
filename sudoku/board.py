from copy import deepcopy
import csv
from pprint import pprint
from typing import IO, List, Optional

from sudoku.cell_group import CellGroup


class Board:
    def __init__(self):
        self.cols = [CellGroup() for _ in range(9)]
        self.rows = [CellGroup() for _ in range(9)]
        self.boxes = [CellGroup() for _ in range(9)]
        self.full_board = [[0] * 9 for _ in range(9)]
        self.solved_board: Optional[List[List[int]]] = None

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

    def clear_value_at(self, col_idx: int, row_idx: int) -> None:
        value = self.full_board[row_idx - 1][col_idx - 1]

        self.cols[col_idx - 1].remove(value)
        self.rows[row_idx - 1].remove(value)
        self.boxes[(col_idx - 1) // 3 + 3 * ((row_idx - 1) // 3)].remove(value)
        self.full_board[row_idx - 1][col_idx - 1] = 0

    def is_empty_at(self, col_idx: int, row_idx: int) -> bool:
        return self.full_board[row_idx - 1][col_idx - 1] == 0

    def print_solution(self, output_stream: IO = None) -> None:
        pprint(self.solved_board, output_stream)

    def load_file(self, board_file: IO) -> None:
        reader = csv.reader(board_file)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                if value:
                    self.set_value_at(col_idx, row_idx, int(value))

    def solve(self) -> None:
        for row_idx in range(1, 10):
            for col_idx in range(1, 10):
                if not self.is_empty_at(col_idx, row_idx):
                    continue

                for value in range(1, 10):
                    if self.set_value_at(col_idx, row_idx, value):
                        self.solve()
                        self.clear_value_at(col_idx, row_idx)
                return
        # Save the state before the recursion unwinds and resets the `full_board`
        self.solved_board = deepcopy(self.full_board)
