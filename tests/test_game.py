import unittest
from src.game import Game

class TestGame(unittest.TestCase):
    def test_switch_turn(self):
        game = Game(3, 'simple', 'human', 'ai')
        current_player = game.get_current_player()
        game.switch_turn()
        next_player = game.get_current_player()

        self.assertNotEqual(current_player, next_player)
        game.switch_turn()
        self.assertEqual(current_player, game.get_current_player())

    if __name__ == '__main__':
        unittest.main()