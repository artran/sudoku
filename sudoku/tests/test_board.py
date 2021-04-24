import unittest

from assertpy import assert_that

from sudoku.board import Board


class MyTestCase(unittest.TestCase):
    def test_new_board_has_nine_cols(self):
        board = Board()
        assert_that(board.cols).is_length(9)

    def test_new_board_has_nine_rows(self):
        board = Board()
        assert_that(board.rows).is_length(9)

    def test_new_board_has_nine_boxes(self):
        board = Board()
        assert_that(board.boxes).is_length(9)

    def test_setting_value_puts_value_in_correct_box(self):
        test_data = [
            # (col, row, box),
            (3, 3, 1),
            (5, 2, 2),
            (7, 3, 3),
            (2, 6, 4),
            (6, 4, 5),
            (8, 5, 6),
            (2, 8, 7),
            (4, 7, 8),
            (9, 8, 9)
        ]

        for item in test_data:
            with self.subTest(f'{item[0]}, {item[1]} -> {item[2]}', item=item):
                board = Board()
                board.set_value_at(item[0], item[1], 9)

                assert_that(board.boxes[item[2] - 1].possible(9)).is_false()
