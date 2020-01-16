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
        self.judge = TicTacToeJudge(self.board)
        self.turn = TicTacToe.PLAYER_ONE
        self.winner = None
        self.state = GameState.DURING

    def move(self, row, col):
        if self.is_game_finished():
            raise Exception('The game is finished.')

        if not self.__is_empty_cell(col, row):
            raise Exception('The cell is already taken.')

        self.board[row][col] = self.turn
        if self.judge.is_any_winner():
            self.winner = self.judge.get_winner()
            self.state = GameState.FINISHED
        elif self.judge.is_board_filled():
            self.state = GameState.FINISHED
        else:
            self.__change_player_turn()

    def is_game_finished(self):
        return self.state == GameState.FINISHED

    def __is_empty_cell(self, col, row):
        return self.board[row][col] != TicTacToe.PLAYER_ONE and self.board[row][col] != TicTacToe.PLAYER_TWO

    def __change_player_turn(self):
        self.turn *= -1

    def winner(self):
        return None if self.winner is None \
            else Player.PLAYER_ONE if self.winner == self.PLAYER_ONE else Player.PLAYER_TWO

