import random
import screen


class GameStats:
    def __init__(self):
        if input("Quieres jugar una partida de 21?: [si/no]: ") != "no":
            self.start_game = True
        else:
            self.start_game = False
        self.deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.user_cards = [random.choice(self.deck), random.choice(self.deck)]
        self.computer_cards = [random.choice(self.deck), random.choice(self.deck)]

    def ask_for_cards(self, player_cards):
        screen.clear()
        if sum(player_cards) > 21:
            if 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)

        if sum(player_cards) < 21:
            if player_cards == self.user_cards:
                print(f"Tus cartas son: {self.user_cards}, puntuacion actual: {sum(self.user_cards)}")
                print(f"primera carta de la computadora: {self.computer_cards[0]}")
                if input("escribe 'si' para agarrar una carta, escribe 'no' para pasar: ") != "no":
                    self.user_cards.append(random.choice(self.deck))
                    return True
                else:
                    return False
            else:
                if sum(self.computer_cards) <= sum(self.user_cards) < 21:
                    self.computer_cards.append(random.choice(self.deck))
                    return True
                else:
                    return False
        return False

    def check_winner(self):
        print(f"Tus cartas finales son: {self.user_cards}, tu puntuacion final fue: {sum(self.user_cards)}")
        print(f"Cartas finales de la computadora: {self.computer_cards}, "
              f"puntuacion final de la computadora: {sum(self.computer_cards)}")
        if 21 >= sum(self.user_cards) > sum(self.computer_cards) or sum(self.computer_cards) > 21:
            print("ganaste! eres la mera riata 😍")
        elif sum(self.user_cards) == sum(self.computer_cards):
            print("Fue un empate 🙃")
        else:
            print("La maquina gano 😳")

