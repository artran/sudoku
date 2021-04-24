from typing import Iterable

from sudoku.cell import Cell


class CellGroup:
    def __init__(self, cell_values: Iterable[int]):
        self._cells = [Cell(n) for n in cell_values]

        if len(self._cells) != 9:
            raise ValueError('Must be nine int values')

    def possible(self, candidate: int) -> bool:
        return all(cell.value != candidate for cell in self._cells)
