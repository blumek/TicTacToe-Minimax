import math

from TicTacToe import TicTacToe


class TicTacToeAI(TicTacToe):
    def __init__(self, board=None):
        super().__init__()
        if board is not None:
            self._board = board

    def ai_move(self):
        row, col = self.__get_next_move_cell()
        self.move(row, col)

    def __get_next_move_cell(self):
        max_ = -math.inf
        pos = None

        alpha = -math.inf
        beta = math.inf

        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != 0:
                    continue

                self._board[row][col] = 1
                eval_ = self.__minimizing_player(alpha, beta)
                self._board[row][col] = 0
                if eval_ > max_:
                    max_ = eval_
                    pos = row, col

                alpha = max(alpha, eval_)
                if beta <= alpha:
                    return pos

        return pos

    def __maximizing_player(self, alpha, beta):
        if self._is_game_finished():
            return self.__get_weight()

        max_eval = -math.inf
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != 0:
                    continue

                self._board[row][col] = self._Board.PLAYER_ONE
                eval_ = self.__minimizing_player(alpha, beta)
                self._board[row][col] = 0
                max_eval = max(max_eval, eval_)
                alpha = max(alpha, eval_)
                if beta <= alpha:
                    return max_eval

        return max_eval

    def __get_weight(self):
        return self._get_winner() * self.__count_empty_cells()

    def __count_empty_cells(self):
        empty_cells = 0
        for row in range(self._board_size):
            for col in range(self._board_size):
                if self._is_empty_cell(row, col):
                    empty_cells += 1
        return empty_cells

    def __minimizing_player(self, alpha, beta):
        if self._is_game_finished():
            return self.__get_weight()

        min_eval = math.inf
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != 0:
                    continue

                self._board[row][col] = self._Board.PLAYER_TWO
                eval_ = self.__maximizing_player(alpha, beta)
                self._board[row][col] = 0
                min_eval = min(min_eval, eval_)
                beta = min(beta, eval_)
                if beta <= alpha:
                    return min_eval

        return min_eval
