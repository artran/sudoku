from itertools import repeat
import unittest

from assertpy import assert_that, fail

from sudoku.cell_group import CellGroup


class CellGroupTestCase(unittest.TestCase):
    def test_iterator_must_have_9_elements(self):
        for i in range(12):
            with self.subTest('Only 9 elements are acceptable', i=i):
                if i != 9:
                    assert_that(CellGroup).raises(ValueError).when_called_with(repeat(0, i))
                else:
                    try:
                        CellGroup(repeat(0, i))
                    except ValueError:
                        fail('9 elements should be acceptable')

    def test_possible_returns_true_if_number_is_possible(self):
        cell_group = CellGroup(range(9))  # 1 cell is blank and only 9 is missing

        for i in range(1, 10):
            with self.subTest('Only 9 should be possible', i=i):
                if i != 9:
                    assert_that(cell_group.possible(i)).is_false()
                else:
                    assert_that(cell_group.possible(i)).is_true()
