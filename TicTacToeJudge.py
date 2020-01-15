class TicTacToeJudge:
    def __init__(self, board):
        self.board = board

    def is_game_finished(self):
        return self.is_board_filled() or self.is_any_winner()

    def is_board_filled(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False

        return True

    def is_any_winner(self):
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
            for j in range(len(self.board[i])):
                col_value += self.board[i][j]
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