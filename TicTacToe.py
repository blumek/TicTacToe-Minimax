from GameState import GameState
from Player import Player


class TicTacToe:
    PLAYER_ONE = 1
    PLAYER_TWO = -1
    DRAW = 0

    def __init__(self):
        self.board = [
            [0] * 3,
            [0] * 3,
            [0] * 3,
        ]
        self.turn = TicTacToe.PLAYER_ONE

    def move(self, row, col):
        if self._is_game_finished():
            raise Exception('The game is finished.')

        if not self.__is_empty_cell(col, row):
            raise Exception('The cell is already taken.')

        self.board[row][col] = self.turn
        if not self.__is_any_winner():
            self.__change_player_turn()

    def __is_empty_cell(self, col, row):
        return self.board[row][col] != TicTacToe.PLAYER_ONE and self.board[row][col] != TicTacToe.PLAYER_TWO

    def __change_player_turn(self):
        self.turn *= -1

    def winner(self):
        return self._get_winner()

    def _is_game_finished(self):
        return self.__is_board_filled() or self.__is_any_winner()

    def __is_board_filled(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
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
        for row in self.board:
            if self.__is_row_winner(sum(row)):
                return True
        return False

    @staticmethod
    def __is_row_winner(row_value):
        return row_value == 1 * 3 or row_value == -1 * 3

    def __is_any_col_winner(self):
        for i in range(len(self.board)):
            col_value = 0
            for j in range(len(self.board)):
                col_value += self.board[j][i]
            if self.__is_col_winner(col_value):
                return True
        return False

    @staticmethod
    def __is_col_winner(col_value):
        return col_value == 1 * 3 or col_value == -1 * 3

    def __is_any_diagonal_winner(self):
        first_diagonal_value = 0
        second_diagonal_value = 0
        for i in range(len(self.board)):
            first_diagonal_value += self.board[i][i]
            second_diagonal_value += self.board[len(self.board) - 1 - i][i]

        if self.__is_diagonal_winner(first_diagonal_value):
            return True

        if self.__is_diagonal_winner(second_diagonal_value):
            return True

        return False

    @staticmethod
    def __is_diagonal_winner(diagonal_value):
        return diagonal_value == 1 * 3 or \
               diagonal_value == -1 * 3

    def _get_winner(self):
        for row in self.board:
            row_sum = sum(row)
            if row_sum == 3:
                return 1
            elif row_sum == -3:
                return -1

        for i in range(len(self.board)):
            col_value = 0
            for j in range(len(self.board)):
                col_value += self.board[j][i]
            if col_value == 3:
                return 1
            elif col_value == -3:
                return -1

        first_diagonal_value = 0
        second_diagonal_value = 0
        for i in range(len(self.board)):
            first_diagonal_value += self.board[i][i]
            second_diagonal_value += self.board[len(self.board) - 1 - i][i]
        if first_diagonal_value == 3 or second_diagonal_value == 3:
            return 1
        elif first_diagonal_value == -3 or second_diagonal_value == -3:
            return -1

        return 0
