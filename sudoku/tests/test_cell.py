import unittest
from assertpy import assert_that, fail, soft_assertions

from sudoku.cell import Cell


class CellTestCase(unittest.TestCase):
    def test_cell_is_initially_empty(self):
        cell = Cell()
        assert_that(cell).has_value(0)

    def test_the_value_can_be_set_to_an_integer(self):
        cell = Cell()
        cell.value = 1

        assert_that(cell).has_value(1)

    def test_cell_can_be_initialised_with_value_between_0_and_9(self):
        for i in range(10):
            with self.subTest('Values from 0 to 9 should be acceptable', i=i):
                cell = Cell(i)
                assert_that(cell).has_value(i)

        for i in range(10):
            cell = Cell()
            with self.subTest('Values from 0 to 9 should be acceptable', i=i):
                cell.value = i
                assert_that(cell).has_value(i)

    def test_cell_rejects_values_less_than_zero(self):
        with soft_assertions():
            assert_that(Cell).raises(ValueError).when_called_with(-1)

            try:
                cell = Cell()
                cell.value = -1
                fail('-1 is not acceptable')
            except ValueError:
                pass

    def test_cell_rejects_values_more_than_nine(self):
        with soft_assertions():
            assert_that(Cell).raises(ValueError).when_called_with(10)

            try:
                cell = Cell()
                cell.value = 10
                fail('10 is not acceptable')
            except ValueError:
                pass

    def test_rejects_non_integer(self):
        assert_that(Cell).raises(ValueError).when_called_with('x')
