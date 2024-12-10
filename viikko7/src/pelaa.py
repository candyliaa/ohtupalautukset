from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class Pelaa:
    def __init__(self):
        pass

    def pelaa(self):
        self.tuomari = Tuomari()
        p1_move = input("Ensimmäisen pelaajan siirto: ")
        p2_move = self.player2_move()
        while self._onko_ok_siirto(p1_move) and self._onko_ok_siirto(p2_move):
            self.tuomari.kirjaa_siirto(p1_move, p2_move)
            print(self.tuomari)

            p1_move = input("Ensimmäisen pelaajan siirto: ")
            p2_move = self.player2_move()

            self.print_ai_move(p2_move)

        print("Kiitos!")
        print(self.tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"


class PelaaAI(Pelaa):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def print_ai_move(self, move):
        print(f"Tietokone valitsi: {move}")

    def player2_move(self):
        return self.tekoaly.anna_siirto()


class PelaaParempiAI(Pelaa):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def print_ai_move(self, move):
        print(f"Tietokone valitsi: {move}")

    def player2_move(self):
        return self.tekoaly.anna_siirto()


class PelaaPelaaja(Pelaa):
    def player2_move(self):
        return input("Toisen pelaajan siirto: ")

    def print_ai_move(self, move):
        pass
