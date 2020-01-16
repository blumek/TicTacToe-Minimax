import math

from TicTacToe import TicTacToe
from TicTacToeJudge import TicTacToeJudge


class TicTacToeAI:
    def __init__(self, board):
        self.board = board
        self.__judge = TicTacToeJudge(self.board)

    def next_move(self):
        max_ = -math.inf
        pos = None

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    continue
                self.board[row][col] = 1
                eval_ = self.minimax_maximizing_player()
                self.board[row][col] = 0
                if eval_ > max_:
                    max_ = eval_
                    pos = (row, col)

        return pos

    def minimax_maximizing_player(self):
        if self.__judge.is_game_finished():
            return self.get_weight()

        max_eval = -math.inf
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    continue

                self.board[row][col] = TicTacToe.PLAYER_ONE
                eval_ = self.minimax_minimizing_player()
                self.board[row][col] = 0
                max_eval = max(max_eval, eval_)
        return max_eval

    def get_weight(self):
        weight = self.__judge.get_winner()
        if weight == TicTacToe.PLAYER_ONE:
            return -1
        elif weight == TicTacToe.PLAYER_TWO:
            return 1
        else:
            return 0

    def minimax_minimizing_player(self):
        if self.__judge.is_game_finished():
            return self.get_weight()

        min_eval = math.inf
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    continue

                self.board[row][col] = TicTacToe.PLAYER_TWO
                eval_ = self.minimax_maximizing_player()
                self.board[row][col] = 0
                min_eval = min(min_eval, eval_)
        return min_eval
