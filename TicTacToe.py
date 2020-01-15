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
        self.__turn = TicTacToe.PLAYER_ONE
        self.__winner = None
        self.__state = GameState.DURING

    def move(self, row, col):
        if self.is_game_finished():
            raise Exception('The game is finished.')

        if not self.__is_empty_cell(col, row):
            raise Exception('The cell is already taken.')

        self.board[row][col] = self.__turn
        if self.__is_any_winner():
            self.__winner = self.__turn
            self.__state = GameState.FINISHED
        elif self.__is_board_filled():
            self.__state = GameState.FINISHED
        else:
            self.__change_player_turn()

    def is_game_finished(self):
        return self.__state == GameState.FINISHED

    def __is_empty_cell(self, col, row):
        return self.board[row][col] != TicTacToe.PLAYER_ONE and self.board[row][col] != TicTacToe.PLAYER_TWO

    def __is_board_filled(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False

        return True

    def __change_player_turn(self):
        self.__turn *= -1

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

    @classmethod
    def __is_row_winner(cls, row_value):
        return row_value == cls.PLAYER_ONE * 3 or row_value == cls.PLAYER_TWO * 3

    def __is_any_col_winner(self):
        for i in range(len(self.board)):
            col_value = 0
            for j in range(len(self.board[i])):
                col_value += self.board[i][j]
            if self.__is_col_winner(col_value):
                return True
        return False

    @classmethod
    def __is_col_winner(cls, col_value):
        return col_value == cls.PLAYER_ONE * 3 or col_value == cls.PLAYER_TWO * 3

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

    @classmethod
    def __is_diagonal_winner(cls, diagonal_value):
        return diagonal_value == cls.PLAYER_ONE * 3 or \
               diagonal_value == cls.PLAYER_TWO * 3

    @property
    def winner(self):
        return None if self.__winner is None \
            else Player.PLAYER_ONE if self.__winner == self.PLAYER_ONE else Player.PLAYER_TWO
