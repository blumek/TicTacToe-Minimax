class TicTacToe:
    class _Board:
        EMPTY_CELL = 0
        PLAYER_ONE = 1
        PLAYER_TWO = -1

    def __init__(self, player_one_sign='X', player_two_sign='O', empty_cell_sign=' '):
        self._board_size = 3
        self._board = [
            [self._Board.EMPTY_CELL] * self._board_size,
            [self._Board.EMPTY_CELL] * self._board_size,
            [self._Board.EMPTY_CELL] * self._board_size,
        ]

        self.__player_one_sign = player_one_sign
        self.__player_two_sign = player_two_sign
        self.__empty_cell_sign = empty_cell_sign

        self.__turn = self._Board.PLAYER_ONE

    @property
    def board(self):
        if self.__player_one_sign == self._Board.PLAYER_ONE and self.__player_two_sign == self._Board.PLAYER_TWO:
            return list(self._board)

        return self.convert_with_player_signs()

    def convert_with_player_signs(self):
        board = []
        for i in range(self._board_size):
            row = []
            for j in range(self._board_size):
                if self._board[i][j] == self._Board.PLAYER_ONE:
                    row.append(self.__player_one_sign)
                elif self._board[i][j] == self._Board.PLAYER_TWO:
                    row.append(self.__player_two_sign)
                else:
                    row.append(self.__empty_cell_sign)
            board.append(row)
        return board

    def move(self, row, col):
        if self._is_game_finished():
            raise Exception('The game is finished.')

        if not self._is_empty_cell(row, col):
            raise Exception('The cell is already taken.')

        self._board[row][col] = self.__turn
        if not self.__is_any_winner():
            self.__change_player_turn()

    def _is_empty_cell(self, row, col):
        return self._board[row][col] == self._Board.EMPTY_CELL

    def __change_player_turn(self):
        self.__turn *= -1

    def winner(self):
        winner = self._get_winner()
        return self.__player_one_sign if winner == self._Board.PLAYER_ONE \
            else self.__player_two_sign if winner == self._Board.PLAYER_TWO else None

    def _is_game_finished(self):
        return self.__is_board_filled() or self.__is_any_winner()

    def __is_board_filled(self):
        for row in self._board:
            for cell in row:
                if cell == self._Board.EMPTY_CELL:
                    return False

        return True

    def __is_any_winner(self):
        if self._get_winner() == self._Board.PLAYER_ONE or \
                self._get_winner() == self._Board.PLAYER_TWO:
            return True

        return False

    def _get_winner(self):
        row_winner = self.__get_row_winner()
        if row_winner != self._Board.EMPTY_CELL:
            return row_winner

        col_winner = self.__get_col_winner()
        if col_winner != self._Board.EMPTY_CELL:
            return col_winner

        diagonal_winner = self.__get_diagonal_winner()
        if diagonal_winner != self._Board.EMPTY_CELL:
            return diagonal_winner

        return self._Board.EMPTY_CELL

    def __get_row_winner(self):
        for row in self._board:
            row_sum = sum(row)
            if self.__is_player_one_win_pattern(row_sum):
                return self._Board.PLAYER_ONE
            elif self.__is_player_two_win_pattern(row_sum):
                return self._Board.PLAYER_TWO

        return self._Board.EMPTY_CELL

    def __is_player_one_win_pattern(self, pattern):
        return pattern == self._Board.PLAYER_ONE * self._board_size

    def __is_player_two_win_pattern(self, pattern):
        return pattern == self._Board.PLAYER_TWO * self._board_size

    def __get_col_winner(self):
        for i in range(self._board_size):
            col_value = self._Board.EMPTY_CELL
            for j in range(self._board_size):
                col_value += self._board[j][i]
            if self.__is_player_one_win_pattern(col_value):
                return self._Board.PLAYER_ONE
            elif self.__is_player_two_win_pattern(col_value):
                return self._Board.PLAYER_TWO

        return self._Board.EMPTY_CELL

    def __get_diagonal_winner(self):
        first_diagonal_value = self._Board.EMPTY_CELL
        second_diagonal_value = self._Board.EMPTY_CELL
        for i in range(self._board_size):
            first_diagonal_value += self._board[i][i]
            second_diagonal_value += self._board[-i - 1][i]

        if self.__is_player_one_win_pattern(first_diagonal_value) or \
                self.__is_player_one_win_pattern(second_diagonal_value):
            return self._Board.PLAYER_ONE
        elif self.__is_player_two_win_pattern(first_diagonal_value) or \
                self.__is_player_two_win_pattern(second_diagonal_value):
            return self._Board.PLAYER_TWO
        else:
            return self._Board.EMPTY_CELL
