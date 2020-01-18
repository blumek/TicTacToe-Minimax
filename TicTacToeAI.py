import math

from TicTacToe import TicTacToe


class TicTacToeAI(TicTacToe):
    def __init__(self, board=None):
        super().__init__()
        if board is not None:
            self._board = board

    def move(self, row, col):
        if self._turn != self._Board.PLAYER_TWO:
            raise Exception("Currently it is computer's turn. Player cannot make a move now.")

        super().move(row, col)

    def ai_move(self):
        if self._turn != self._Board.PLAYER_ONE:
            raise Exception("Currently it is player's turn. Computer cannot make a move now.")

        row, col = self.__get_next_move_cell()
        super().move(row, col)

    def __get_next_move_cell(self):
        max_weight = -math.inf
        pos = None
        alpha = -math.inf
        beta = math.inf

        for row in range(self._board_size):
            for col in range(self._board_size):
                if not self._is_empty_cell(row, col):
                    continue

                self._board[row][col] = self._Board.PLAYER_ONE
                weight = self.__minimizing_player(alpha, beta)
                self._board[row][col] = self._Board.EMPTY_CELL

                if weight > max_weight:
                    max_weight = weight
                    pos = row, col

                alpha = max(alpha, weight)
                if beta <= alpha:
                    return pos

        return pos

    def __maximizing_player(self, alpha, beta):
        if self._is_game_finished():
            return self.__get_weight()

        max_weight = -math.inf
        for row in range(self._board_size):
            for col in range(self._board_size):
                if not self._is_empty_cell(row, col):
                    continue

                self._board[row][col] = self._Board.PLAYER_ONE
                weight = self.__minimizing_player(alpha, beta)
                self._board[row][col] = self._Board.EMPTY_CELL

                max_weight = max(max_weight, weight)
                alpha = max(alpha, weight)
                if beta <= alpha:
                    return max_weight

        return max_weight

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

        min_weight = math.inf
        for row in range(self._board_size):
            for col in range(self._board_size):
                if not self._is_empty_cell(row, col):
                    continue

                self._board[row][col] = self._Board.PLAYER_TWO
                weight = self.__maximizing_player(alpha, beta)
                self._board[row][col] = self._Board.EMPTY_CELL

                min_weight = min(min_weight, weight)
                beta = min(beta, weight)
                if beta <= alpha:
                    return min_weight

        return min_weight
