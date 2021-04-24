from io import StringIO
import unittest

from assertpy import assert_that, soft_assertions

from sudoku.board import Board


class BoardTestCase(unittest.TestCase):
    def test_new_board_has_nine_cols(self):
        board = Board()
        assert_that(board.cols).is_length(9)

    def test_new_board_has_nine_rows(self):
        board = Board()
        assert_that(board.rows).is_length(9)

    def test_new_board_has_nine_boxes(self):
        board = Board()
        assert_that(board.boxes).is_length(9)

    def test_setting_value_puts_value_in_correct_groups(self):
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

                with soft_assertions():
                    assert_that(board.cols[item[0] - 1]).contains(9)
                    assert_that(board.rows[item[1] - 1]).contains(9)
                    assert_that(board.boxes[item[2] - 1]).contains(9)

    def test_setting_acceptable_value_returns_true(self):
        board = Board()
        assert_that(board.set_value_at(1, 1, 1)).is_true()

    def test_setting_unacceptable_value_returns_true(self):
        board = Board()
        board.set_value_at(1, 1, 1)
        assert_that(board.set_value_at(2, 1, 1)).is_false()

    def test_setting_unacceptable_value_leaves_state_unchanged(self):
        board = Board()
        board.set_value_at(1, 1, 1)
        initial_state = str(board)

        board.set_value_at(2, 1, 1)
        assert_that(str(board)).is_equal_to(initial_state)

    def test_setting_acceptable_value_updates_board(self):
        expected_board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board = Board()

        board.set_value_at(1, 1, 1)

        assert_that(board.full_board).is_equal_to(expected_board)

    def test_setting_unacceptable_value_does_not_update_board(self):
        expected_board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        board = Board()

        board.set_value_at(1, 1, 1)
        board.set_value_at(2, 1, 1)

        assert_that(board.full_board).is_equal_to(expected_board)

    def test_the_board_can_print_itself(self):
        expected_output = '[[1, 0, 0, 0, 0, 0, 0, 0, 0],\n' \
                          ' [0, 0, 0, 0, 0, 0, 0, 0, 0],\n' \
                          ' [0, 0, 0, 0, 0, 0, 0, 0, 0],\n' \
                          ' [0, 0, 0, 0, 0, 0, 0, 0, 0],\n' \
                          ' [0, 0, 0, 0, 0, 0, 0, 0, 0],\n' \
                          ' [0, 0, 0, 0, 0, 0, 0, 0, 0],\n' \
                          ' [0, 0, 0, 0, 0, 0, 0, 0, 0],\n' \
                          ' [0, 0, 0, 0, 0, 0, 0, 0, 0],\n' \
                          ' [0, 0, 0, 0, 0, 0, 0, 0, 0]]\n'
        output_stream = StringIO()
        board = Board()
        board.set_value_at(1, 1, 1)
        board.print(output_stream)

        assert_that(output_stream.getvalue()).is_equal_to(expected_output)

    def test_the_board_can_be_initialised_from_csv_file(self):
        board_file = StringIO('6,,,,,3,,,\n'
                              ',9,,8,6,7,3,,\n'
                              ',3,7,2,5,,6,,\n'
                              ',,4,1,3,,2,,\n'
                              '3,,9,,,,1,,5\n'
                              ',,8,,2,9,4,,\n'
                              ',,5,,4,1,7,2,\n'
                              ',,3,7,9,6,,8,\n'
                              ',,,5,,,,,1\n')
        expected_board = [
            [6, 0, 0, 0, 0, 3, 0, 0, 0],
            [0, 9, 0, 8, 6, 7, 3, 0, 0],
            [0, 3, 7, 2, 5, 0, 6, 0, 0],
            [0, 0, 4, 1, 3, 0, 2, 0, 0],
            [3, 0, 9, 0, 0, 0, 1, 0, 5],
            [0, 0, 8, 0, 2, 9, 4, 0, 0],
            [0, 0, 5, 0, 4, 1, 7, 2, 0],
            [0, 0, 3, 7, 9, 6, 0, 8, 0],
            [0, 0, 0, 5, 0, 0, 0, 0, 1]
        ]

        board = Board()
        board.load_file(board_file)

        assert_that(board.full_board).is_equal_to(expected_board)
