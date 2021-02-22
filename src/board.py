import numpy as np

import setting


class Board:
    def __init__(self):
        self.board = np.zeros((setting.COLUMN, setting.COLUMN))

    def init(self):
        center = setting.COLUMN // 2
        self.board[center-1][center-1] = 1
        self.board[center][center] = 1
        self.board[center-1][center] = 2
        self.board[center][center-1] = 2

    def check_done(self):
        pass

    def get_state(self):
        state = 0
        num = 1
        for row in self.board:
            for column in row:
                state += column * num
                num *= 3

    def step(self, action, player_idx):
        pass

    def __repr__(self):
        txt = ''
        for row in self.board:
            for column in row:
                if column == 0:
                    txt += '  '
                elif column == 1:
                    txt += '● '
                elif column == 2:
                    txt += '○ '
            txt += '\n'
        return txt
