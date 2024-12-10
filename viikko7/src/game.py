from pelaa import PelaaPelaaja
from pelaa import PelaaAI
from pelaa import PelaaParempiAI


class Game:
    def __init__(self, gametype):
        self.gametype = gametype

    @staticmethod
    def create_pvp_game():
        return PelaaPelaaja()

    @staticmethod
    def create_ai_game():
        return PelaaAI()

    @staticmethod
    def create_difficult_ai_game():
        return PelaaParempiAI()
