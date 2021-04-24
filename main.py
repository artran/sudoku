#!/usr/bin/env python3

from io import StringIO

from sudoku.board import Board

if __name__ == '__main__':
    board_file = StringIO('6,,,,,3,,,\n'
                          ',9,,8,6,7,3,,\n'
                          ',3,7,2,5,,6,,\n'
                          ',,4,1,3,,2,,\n'
                          '3,,9,,,,1,,5\n'
                          ',,8,,2,9,4,,\n'
                          ',,5,,4,1,7,2,\n'
                          ',,3,7,9,6,,8,\n'
                          ',,,5,,,,,1\n')

    board = Board()
    board.load_file(board_file)
    board.solve()
