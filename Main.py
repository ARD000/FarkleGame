# -*- coding: utf-8 -*-
"""
@author: ammad
"""

from FarkleGame import print_rules, start_game, player_turn, display_scores

def main() -> None:
    print_rules()
    
    game_started, player1, player2 = start_game()
    
    if game_started:
        print("The game has started!")
        players = [player1, player2]
        while all(player.score < 10000 for player in players):
            for i, player in enumerate(players):
                players[i] = player_turn(player)
                display_scores(players)
                if players[i].score >= 10000:
                    print(f"{players[i].name} wins with a score of {players[i].score}!")
                    return

if __name__ == "__main__":
    main()

