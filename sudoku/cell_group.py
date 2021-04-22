from typing import Iterable

from sudoku.cell import Cell


class CellGroup:
    def __init__(self, cells: Iterable[Cell]):
        self._cells = cells

    def possible(self, candidate: int) -> bool:
        for cell in self._cells:
            if cell.value == candidate:
                return False
        return True
