class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = self.score_if_equal()
        if not score:
            score = self.score_if_advantage()
            if not score:
                score = self.find_exact_score("")
        return score

    def score_if_equal(self):
        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                score = "Love-All"
            elif self.player1_score == 1:
                score = "Fifteen-All"
            elif self.player1_score == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"
        else:
            return False
        return score

    def score_if_advantage(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            player1_advantage = self.player1_score - self.player2_score

            if player1_advantage == 1:
                score = "Advantage player1"
            elif player1_advantage == -1:
                score = "Advantage player2"
            elif player1_advantage >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            return False
        return score

    def find_exact_score(self, score):
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score = score + "-"
                temp_score = self.player2_score
            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score
