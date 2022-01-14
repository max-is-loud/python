from collections import OrderedDict
from classes import *
from errors import *

# Global Variables
players = {'dealer':Player('dealer')} #Initialize players dict with dealer.

def draw_cards(num,deck,player) -> None:
    
    for i in range(num):
        player.hand.append(deck.cards.pop())
        
    print(f'{num} cards dealt to {player.name}.')

def hand_total(player):
    hand_value = 0
    for card in player1.hand:
        if card.value == 11:
            if hand_value + card.value > 21:
                hand_value += 11
            else: hand_value += 1
        else:
            hand_value += card.value
    return hand_value

def init_players():
    """Initializes players, based in user input."""
    global players
    
    while True:
        num = input("How many players? Enter a number between 1 and 6\n>")
            try:
                num = int(num)
            except ValueError:
                print('Invalid entry, a number between 1 and 6 only.')
                continue
            if 1 <= num <= 6:
                break
            else:
                print('6 players maximum only.')
    
    for x in range(1,num+1):
        players[f'player_{x}'] = Player(input(f'Player {x}, enter your name:\n>'))
    print(f'{num} players playing!')

def place_bets(self, amount):
        bet 
        try:
            pass
        except:
            pass