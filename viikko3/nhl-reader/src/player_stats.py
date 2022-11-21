class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()

        players.sort(key=lambda x: x.goals + x.assists, reverse=True)

        return players
        