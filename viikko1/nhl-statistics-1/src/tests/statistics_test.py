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

    def test_search_loytaa_pelaajan(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_search_palauttaa_none(self):
        player = self.statistics.search("Matikainen")
        self.assertEqual(player, None)

    def test_team_palauttaa_oikeat_pelaajat(self):
        edm_players = self.statistics.team("EDM")
        for player in edm_players:
            self.assertEqual(player.team, "EDM")


    def test_top_scorers(self):
        players = self.statistics.top_scorers(4)
        names = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        
        for index, player in enumerate(players):
            self.assertEqual(player.name, names[index])

