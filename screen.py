import os
from art import logo


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)



