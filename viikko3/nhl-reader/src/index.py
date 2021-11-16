from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    player_reader = PlayerReader(url)
    player_stats = PlayerStats(player_reader)
    players = player_stats.top_scorers_by_nationality("FIN")
    
    for player in players:
        print(player)
    

if __name__ == "__main__":
    main()
