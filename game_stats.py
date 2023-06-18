import random
import screen


class GameStats:
    def __init__(self):
        if input("Do you want to play a game of blackjack?[Y/n]: ") == "Y":
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
                print(f"Your cards: {self.user_cards}, current score: {sum(self.user_cards)}")
                print(f"Computer's first card: {self.computer_cards[0]}")
                if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
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
        print(f"Your final cards: {self.user_cards}, Your final score: {sum(self.user_cards)}")
        print(f"Computer final cards: {self.computer_cards}, Computer's final score: {sum(self.computer_cards)}")
        if 21 >= sum(self.user_cards) > sum(self.computer_cards) or sum(self.computer_cards) > 21:
            print("user win")
        elif sum(self.user_cards) == sum(self.computer_cards):
            print("it's a draw")
        else:
            print("the machine win")
