import math

from TicTacToe import TicTacToe


class TicTacToeAI(TicTacToe):
    def __init__(self, board=None):
        super().__init__()
        if board is not None:
            self.board = board

    def ai_move(self):
        row, col = self.get_next_move_cell()
        self.move(row, col)

    def get_next_move_cell(self):
        max_ = -math.inf
        pos = None

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    continue
                self.board[row][col] = 1
                eval_ = self.minimax_minimizing_player()
                self.board[row][col] = 0
                if eval_ > max_:
                    max_ = eval_
                    pos = row, col

        return pos

    def minimax_maximizing_player(self):
        if self._is_game_finished():
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
        return self._get_winner()

    def minimax_minimizing_player(self):
        if self._is_game_finished():
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
