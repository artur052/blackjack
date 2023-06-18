from Player_Desicions import PlayerDecisions
from game_stats import GameStats
player = PlayerDecisions()
game = GameStats()
turn = 1

while game.start_game:
    while player.still_playing:
        if not game.ask_for_cards(player_cards=game.user_cards if turn == 1 else game.computer_cards):
            if sum(game.user_cards) < 21:
                turn += 1
                if turn > 2:
                    player.still_playing = False
            else:
                player.still_playing = False
    game.check_winner()
    game = GameStats()
    player = PlayerDecisions()
    turn = 1
