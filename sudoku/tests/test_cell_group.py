import unittest

from assertpy import assert_that

from sudoku.cell import Cell
from sudoku.cell_group import CellGroup


class CellGroupTestCase(unittest.TestCase):
    def test_possible_returns_true_if_number_is_possible(self):
        cells = [Cell(n) for n in range(9)]  # 1 cell is blank and only 9 is missing
        cell_group = CellGroup(cells)

        for i in range(1, 10):
            with self.subTest('Only 9 should be possible', i=i):
                if i != 9:
                    assert_that(cell_group.possible(i)).is_false()
                else:
                    assert_that(cell_group.possible(i)).is_true()
