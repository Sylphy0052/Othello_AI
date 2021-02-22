from board import Board


class Environment:
    def __init__(self, player1, player2):
        self.player1, self.player2 = player1, player2
        self.board = Board()

    def init(self):
        self.board.init()

    def step(self, player):
        action = player.get_action(self.board.get_state())
        self.board.step(action, player.player_idx)
        return self.board.get_state()

    def train(self, episode):
        is_done = False
        while not is_done:
            for player in [self.player1, self.player2]:
                state = self.step(player)
                if self.board.check_done:
                    is_done = True
                    break
            break
