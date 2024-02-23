from player import CPUPlayer
from card import Card


class TestCPUPlayer:

    def setup(self):
        card = Card([1, 2, 3])
        self.player = CPUPlayer('CPU', card)

    def test_turn(self):
        assert self.player.is_winner is None
        self.player.turn(1)
        assert self.player.is_winner is None
        self.player.turn(10)
        assert self.player.is_winner is None
        self.player.turn(2)
        assert self.player.is_winner is None
        self.player.turn(3)
        assert self.player.is_winner
