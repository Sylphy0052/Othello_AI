

class Player:
    def __init__(self, player_idx):
        self.player_idx = player_idx


class AI(Player):
    def __init__(self, player_idx):
        super().__init__(player_idx)
