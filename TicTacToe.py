from GameState import GameState
from Player import Player
from TicTacToeJudge import TicTacToeJudge


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
        self.__judge = TicTacToeJudge(self.board)
        self.__turn = TicTacToe.PLAYER_ONE
        self.__winner = None
        self.__state = GameState.DURING

    def move(self, row, col):
        if self.is_game_finished():
            raise Exception('The game is finished.')

        if not self.__is_empty_cell(col, row):
            raise Exception('The cell is already taken.')

        self.board[row][col] = self.__turn
        if self.__judge.is_any_winner():
            self.__winner = self.__judge.get_winner()
            self.__state = GameState.FINISHED
        elif self.__judge.is_board_filled():
            self.__state = GameState.FINISHED
        else:
            self.__change_player_turn()

    def is_game_finished(self):
        return self.__state == GameState.FINISHED

    def __is_empty_cell(self, col, row):
        return self.board[row][col] != TicTacToe.PLAYER_ONE and self.board[row][col] != TicTacToe.PLAYER_TWO

    def __change_player_turn(self):
        self.__turn *= -1

    @property
    def winner(self):
        return None if self.__winner is None \
            else Player.PLAYER_ONE if self.__winner == self.PLAYER_ONE else Player.PLAYER_TWO
