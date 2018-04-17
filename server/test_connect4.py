#! /usr/bin/env python3

import unittest

from connect4 import Connect4

class TestConnect4(unittest.TestCase):
    def testCreateWithDefault(self):
        b = Connect4()

    def testCreateWithCustomArgs(self):
        b = Connect4(10, 11)

    def testColumnFull(self):
        b = Connect4()
        b.move(0, '1')
        self.assertFalse(b.column_full(0))
        b.move(0, '1')
        self.assertFalse(b.column_full(0))
        b.move(0, '1')
        self.assertFalse(b.column_full(0))
        b.move(0, '1')
        self.assertFalse(b.column_full(0))
        b.move(0, '1')
        self.assertFalse(b.column_full(0))
        b.move(0, '1')
        self.assertTrue(b.column_full(0))

    def testWinnerVertical(self):
        b = Connect4()
        self.assertFalse(b.winner('1'))
        b.move(0, '1')
        self.assertFalse(b.winner('1'))
        b.move(0, '1')
        self.assertFalse(b.winner('1'))
        b.move(0, '1')
        self.assertFalse(b.winner('1'))
        b.move(0, '1')
        self.assertTrue(b.winner('1'))

    def testWinnerHorizontal(self):
        b = Connect4()
        self.assertFalse(b.winner('1'))
        b.move(0, '1')
        self.assertFalse(b.winner('1'))
        b.move(1, '1')
        self.assertFalse(b.winner('1'))
        b.move(2, '1')
        self.assertFalse(b.winner('1'))
        b.move(3, '1')
        self.assertTrue(b.winner('1'))

    def testWinnerDiagonalBackSlash(self):
        b = Connect4()
        self.assertFalse(b.winner('1'))
        b.move(0, '2')
        b.move(0, '2')
        b.move(0, '2')
        b.move(0, '1')
        self.assertFalse(b.winner('1'))
        b.move(1, '2')
        b.move(1, '2')
        b.move(1, '1')
        self.assertFalse(b.winner('1'))
        b.move(2, '2')
        b.move(2, '1')
        self.assertFalse(b.winner('1'))
        b.move(3, '1')
        self.assertTrue(b.winner('1'))

    def testWinnerDiagonalForwardSlash(self):
        b = Connect4()
        self.assertFalse(b.winner('1'))
        b.move(3, '2')
        b.move(3, '2')
        b.move(3, '2')
        b.move(3, '1')
        self.assertFalse(b.winner('1'))
        b.move(2, '2')
        b.move(2, '2')
        b.move(2, '1')
        self.assertFalse(b.winner('1'))
        b.move(1, '2')
        b.move(1, '1')
        self.assertFalse(b.winner('1'))
        b.move(0, '1')
        self.assertTrue(b.winner('1'))

    def testAvailanleColumns(self):
        b = Connect4()
        self.assertListEqual([0,1,2,3,4,5,6], b.get_available_columns())

        b.move(0, '1')
        b.move(0, '1')
        b.move(0, '1')
        b.move(0, '1')
        b.move(0, '1')
        self.assertListEqual([0,1,2,3,4,5,6], b.get_available_columns())

        b.move(0, '1')
        self.assertListEqual([1,2,3,4,5,6], b.get_available_columns())

        b.move(6, '2')
        b.move(6, '2')
        b.move(6, '2')
        b.move(6, '2')
        b.move(6, '2')
        self.assertListEqual([1,2,3,4,5,6], b.get_available_columns())

        b.move(6, '2')
        self.assertListEqual([1,2,3,4,5], b.get_available_columns())

if __name__ == '__main__':
    unittest.main()
