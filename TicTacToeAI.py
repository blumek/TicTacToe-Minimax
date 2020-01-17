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

        alpha = -math.inf
        beta = math.inf

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    continue

                self.board[row][col] = 1
                eval_ = self.minimax_minimizing_player(alpha, beta)
                self.board[row][col] = 0
                if eval_ > max_:
                    max_ = eval_
                    pos = row, col

                alpha = max(alpha, eval_)
                if beta <= alpha:
                    return pos

        return pos

    def minimax_maximizing_player(self, alpha, beta):
        if self._is_game_finished():
            return self.get_weight()

        max_eval = -math.inf
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    continue

                self.board[row][col] = TicTacToe.PLAYER_ONE
                eval_ = self.minimax_minimizing_player(alpha, beta)
                self.board[row][col] = 0
                max_eval = max(max_eval, eval_)
                alpha = max(alpha, eval_)
                if beta <= alpha:
                    return max_eval

        return max_eval

    def get_weight(self):
        return self._get_winner()

    def minimax_minimizing_player(self, alpha, beta):
        if self._is_game_finished():
            return self.get_weight()

        min_eval = math.inf
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    continue

                self.board[row][col] = TicTacToe.PLAYER_TWO
                eval_ = self.minimax_maximizing_player(alpha, beta)
                self.board[row][col] = 0
                min_eval = min(min_eval, eval_)
                beta = min(beta, eval_)
                if beta <= alpha:
                    return min_eval

        return min_eval
