import unittest
from project.player.advanced import Advanced
from project.player.player import Player
class TestAdvanced(unittest.TestCase):
    def test_init(self):
        a = Advanced('username')
        self.assertEqual(a.username, 'username')
        self.assertEqual(250, a.health)


