TIE_SCORES = {0:"Love-All", 1:"Fifteen-All", 2:"Thirty-All"}
LEAD_SCORES = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._get_tie_score()

        if self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_advantage_score()

        return self._get_lead_score()

    def _get_tie_score(self):
        return TIE_SCORES.get(self.player1_score, "Deuce")

    def _get_advantage_score(self):
        difference = self.player1_score - self.player2_score

        if difference == 1:
            return "Advantage player1"

        if difference == -1:
            return "Advantage player2"

        if difference >= 2:
            return "Win for player1"

        return "Win for player2"

    def _get_lead_score(self):
        return f"{LEAD_SCORES[self.player1_score]}-{LEAD_SCORES[self.player2_score]}"
