import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self._url = url
        self.response = requests.get(self._url).json()

    def get_players(self):
        return self.response


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        player_dicts = self.reader.get_players()
        players = []
        for player_dict in player_dicts:
            if player_dict["nationality"] == nationality:
                player = Player(player_dict)
                players.append(player)
        players_sorted = sorted(
            players, key=lambda p: (p.goals + p.assists), reverse=True
        )
        return players_sorted


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


main()
