import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            player = Player(player_dict)
            players.append(player)

    print("Players from FIN")

    players_sorted = sorted(players, key=lambda p: (p.goals + p.assists), reverse=True)
    for player in players_sorted:
        print(player)


main()
