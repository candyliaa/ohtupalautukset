from game import Game


def main():

    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()

        if vastaus.endswith("a"):
            kaksinpeli = Game.create_pvp_game()
            kaksinpeli.pelaa()

        elif vastaus.endswith("b"):

            yksinpeli = Game.create_ai_game()
            yksinpeli.pelaa()

        elif vastaus.endswith("c"):
            haastava_yksinpeli = Game.create_difficult_ai_game()
            haastava_yksinpeli.pelaa()

        else:
            break


if __name__ == "__main__":
    main()
