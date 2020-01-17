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
        
        self.__player_one_win_pattern = self._Board.PLAYER_ONE * self._board_size
        self.__player_two_win_pattern = self._Board.PLAYER_TWO * self._board_size

        self.__turn = self._Board.PLAYER_ONE

    @property
    def board(self):
        if self.__player_one_sign == self._Board.PLAYER_ONE and self.__player_two_sign == self._Board.PLAYER_TWO:
            return list(self._board)

        board = []
        for i in range(len(self._board)):
            row = []
            for j in range(len(self._board)):
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
        return self._get_winner()

    def _is_game_finished(self):
        return self.__is_board_filled() or self.__is_any_winner()

    def __is_board_filled(self):
        for row in self._board:
            for cell in row:
                if cell == self._Board.EMPTY_CELL:
                    return False

        return True

    def __is_any_winner(self):
        if self.__is_any_row_winner():
            return True

        if self.__is_any_col_winner():
            return True

        if self.__is_any_diagonal_winner():
            return True

        return False

    def __is_any_row_winner(self):
        for row in self._board:
            if self.__is_row_winner(sum(row)):
                return True
        return False

    def __is_row_winner(self, row_value):
        return row_value == self.__player_one_win_pattern or row_value == self.__player_two_win_pattern

    def __is_any_col_winner(self):
        for i in range(len(self._board)):
            col_value = self._Board.EMPTY_CELL
            for j in range(len(self._board)):
                col_value += self._board[j][i]
            if self.__is_col_winner(col_value):
                return True

        return False

    def __is_col_winner(self, col_value):
        return col_value == self.__player_one_win_pattern or col_value == self.__player_two_win_pattern

    def __is_any_diagonal_winner(self):
        first_diagonal_value = self._Board.EMPTY_CELL
        second_diagonal_value = self._Board.EMPTY_CELL
        for i in range(len(self._board)):
            first_diagonal_value += self._board[i][i]
            second_diagonal_value += self._board[-i - 1][i]

        if self.__is_diagonal_winner(first_diagonal_value):
            return True

        if self.__is_diagonal_winner(second_diagonal_value):
            return True

        return False

    def __is_diagonal_winner(self, diagonal_value):
        return diagonal_value == self.__player_one_win_pattern or diagonal_value == self.__player_two_win_pattern

    def _get_winner(self):
        for row in self._board:
            row_sum = sum(row)
            if row_sum == self.__player_one_win_pattern:
                return self._Board.PLAYER_ONE
            elif row_sum == self.__player_two_win_pattern:
                return self._Board.PLAYER_TWO

        for i in range(len(self._board)):
            col_value = self._Board.EMPTY_CELL
            for j in range(len(self._board)):
                col_value += self._board[j][i]
            if col_value == self.__player_one_win_pattern:
                return self._Board.PLAYER_ONE
            elif col_value == self.__player_two_win_pattern:
                return self._Board.PLAYER_TWO

        first_diagonal_value = self._Board.EMPTY_CELL
        second_diagonal_value = self._Board.EMPTY_CELL
        for i in range(len(self._board)):
            first_diagonal_value += self._board[i][i]
            second_diagonal_value += self._board[-i - 1][i]

        if first_diagonal_value == self.__player_one_win_pattern or \
                second_diagonal_value == self.__player_one_win_pattern:
            return self._Board.PLAYER_ONE
        elif first_diagonal_value == self.__player_two_win_pattern or \
                second_diagonal_value == self.__player_two_win_pattern:
            return self._Board.PLAYER_TWO

        return self._Board.EMPTY_CELL
