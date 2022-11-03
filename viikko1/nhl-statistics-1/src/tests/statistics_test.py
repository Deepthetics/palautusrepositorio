import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search_returns_correct_player_if_player_exists(self):
      player = self.statistics.search("Lemieux")
      self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_if_player_does_not_exist(self):
      player = self.statistics.search("Player")
      self.assertEqual(player, None)

    def test_team_returns_correct_list_of_players(self):
      players = self.statistics.team("EDM")
      self.assertEqual(len(players), 3)
      self.assertEqual(players[0].team, "EDM")
      self.assertEqual(players[1].team, "EDM")
      self.assertEqual(players[2].team, "EDM")

    def test_top_returns_correct_ordered_list_of_players(self):
      players = self.statistics.top(3)
      self.assertEqual(len(players), 3)
      self.assertEqual(players[0].points, 35+89)
      self.assertEqual(players[1].points, 45+54)
      self.assertEqual(players[2].points, 42+56)
