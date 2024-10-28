import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


def player_equal(p1, p2, msg):
    if (
        p1.name == p2.name
        and p1.team == p2.team
        and p1.goals == p2.goals
        and p1.assists == p2.assists
    ):
        return True
    return False


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())
        self.addTypeEqualityFunc(Player, player_equal)

    def test_player_exists(self):
        self.assertEqual(self.stats.search("Semenko"), Player("Semenko", "EDM", 4, 12))

    def test_player_does_not_exist(self):
        self.assertEqual(self.stats.search("3458673468573467"), None)

    def test_team_exists(self):
        found = self.stats.team("PIT")
        expected = [Player("Lemieux", "PIT", 45, 54)]
        self.assertEqual(len(found), len(expected))
        for x, y in zip(found, expected):
            self.assertEqual(x, y)

    def test_team_does_not_exist(self):
        self.assertEqual(self.stats.team(""), [])

    def test_top_minus_one(self):
        self.assertEqual(self.stats.top(-1), [])

    def test_top_three(self):
        found = self.stats.top(2)
        expected = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
        ]
        self.assertEqual(len(found), len(expected))
        for x, y in zip(found, expected):
            self.assertEqual(x, y)
