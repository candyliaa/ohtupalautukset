import requests
from rich import print
from rich.table import Table
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
    print("NHL statistics by nationality")
    print(
        "\nSelect season [bright_magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/bright_magenta] "
    )
    season = str(input())
    if season not in [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
    ]:
        print("\nNot a valid season! Exiting program...")
        exit()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    while True:
        print(
            "\nSelect nationality [bright_magenta][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR][/bright_magenta] "
        )
        nationality = str(input())
        if nationality not in [
            "AUT",
            "CZE",
            "AUS",
            "SWE",
            "GER",
            "DEN",
            "SUI",
            "SVK",
            "NOR",
            "RUS",
            "CAN",
            "LAT",
            "BLR",
            "SLO",
            "USA",
            "FIN",
            "GBR",
        ]:
            print("Not a valid nationality! Exiting program...")
            exit()
        table = Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("name", style="blue")
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")
        players = stats.top_scorers_by_nationality(nationality)
        for player in players:
            table.add_row(
                str(player.name),
                str(player.team),
                str(player.goals),
                str(player.assists),
                str((player.goals + player.assists)),
            )
        print(table)


main()
