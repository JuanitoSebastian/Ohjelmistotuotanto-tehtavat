from player import Player
from player_reader import *

class PlayerStats:
    def __init__(self, player_reader):
        self._player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self._player_reader.get_players()
        players = list(filter(lambda player: player.nationality == nationality, players))
        players.sort(key = lambda player: player.assists_and_goals_total(), reverse = True)
        return players