import unittest

from TicTacToeAI import TicTacToeAI


class MyTestCase(unittest.TestCase):
    def test_tic_tac_toe_ai_1(self):
        board = [
            [0, -1, 0],
            [-1, 1, 1],
            [1, 0, -1]
        ]
        tic_tac_toe_ai = TicTacToeAI(board)
        self.assertEqual(tic_tac_toe_ai._TicTacToeAI__get_next_move_cell(), (0, 2))

    def test_tic_tac_toe_ai_2(self):
        board = [
            [1, 0, -1],
            [1, 1, 0],
            [0, -1, -1]
        ]
        tic_tac_toe_ai = TicTacToeAI(board)
        self.assertEqual(tic_tac_toe_ai._TicTacToeAI__get_next_move_cell(), (1, 2))

    def test_tic_tac_toe_ai_3(self):
        board = [
            [1, -1, 1],
            [-1, 1, -1],
            [-1, 0, 0]
        ]
        tic_tac_toe_ai = TicTacToeAI(board)
        self.assertEqual(tic_tac_toe_ai._TicTacToeAI__get_next_move_cell(), (2, 2))

    def test_tic_tac_toe_ai_4(self):
        board = [
            [1, -1, 1],
            [0, -1, -1],
            [0, 1, 0]
        ]
        tic_tac_toe_ai = TicTacToeAI(board)
        self.assertEqual(tic_tac_toe_ai._TicTacToeAI__get_next_move_cell(), (1, 0))

    def test_tic_tac_toe_ai_5(self):
        board = [
            [1, 0, 0],
            [0, -1, 0],
            [-1, 0, 1]
        ]
        tic_tac_toe_ai = TicTacToeAI(board)
        self.assertEqual(tic_tac_toe_ai._TicTacToeAI__get_next_move_cell(), (0, 2))

    def test_tic_tac_toe_ai_6(self):
        board = [
            [0, 1, 0],
            [0, 0, -1],
            [-1, 1, 0]
        ]
        tic_tac_toe_ai = TicTacToeAI(board)
        self.assertEqual(tic_tac_toe_ai._TicTacToeAI__get_next_move_cell(), (1, 1))

    def test_tic_tac_toe_ai_7(self):
        board = [
            [0, 1, -1],
            [0, 0, -1],
            [-1, 1, 1]
        ]
        tic_tac_toe_ai = TicTacToeAI(board)
        self.assertEqual(tic_tac_toe_ai._TicTacToeAI__get_next_move_cell(), (1, 1))


if __name__ == '__main__':
    unittest.main()
