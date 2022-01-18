from shutil import get_terminal_size
from os import system
from time import sleep
from classes import *

# Global Variables
players = {'dealer':Player('dealer')} #Initialize players dict with dealer.

header = {
    # Just for me to keep track my versions.
    'title':   'Blackjack',
    'tag1':    'Written by Maxime Langlois-Morin.',
    'tag2':    'Milestone Project 2 - 2022 Complete Python Bootcamp From Zero to Hero in Python by Pieran Data',
    'version': '0.0.1',
    'date':    'January 14th 2022'
            }

def clear_output():
    system('clear')

def draw_header():
    clear_output()
    print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size() +"\n\n\n\n\n")


def initial_draw(type = 'start'):
    """Runs through the process of dealing initial cards to all players.
    Deals 1 card to player 1 through to the last player, then one to the dealer.
    Repeats process again from player 1 onwards for second card.

    For loop below calls range with the stop number being the length of the
    player list, which is exclusive of the last number - which is fine because
    dealer is ignored.
    """
    if type == 'start':
        cards_dealt = 0
        while cards_dealt < 2:
            for x in range(1,len(players)):
                players[f'player_{x}'].hand = game_deck.draw_card()
                print(f'Player {x} was dealt: {players[f"player_{x}"].show_hand()}')
                print(f'{players[f"player_{x}"].hand_value()}')
            players['dealer'].hand = game_deck.draw_card
            if cards_dealt == 0:
                print(f'Dealer was dealt {players["dealer"].show_hand()}\n{players["dealer"].hand_value()}')
            cards_dealt += 1
    
    else: 
        players.hand = game_deck.draw_card


def init_players():
    """Initializes players, based in user input."""
    global players
    balance = None

    while True:
        balance = input("Enter a starting balance amount between $100 and $1000\n>")
        try:
            balance = int(balance)
        except ValueError:
            print('Invalid entry, a number between $100 and $1000 only.')
            continue
        if 100 <= balance <= 10000:
            break
        else:
            print('Invalid entry, a number between $100 and $1000 only.')
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
        players[f'player_{x}'] = Player(input(f'Player {x}, enter your name:\n>'),balance)
    print(f'{num} players playing!')

def place_bets():
    for player in players:
        if player.balance < 2:
            continue
        else:
            bet = None
            while True:
                bet = input(f'Player: {player.name}, place your bet\n(Bets must be between $2 and $10)\n>')
                try:
                    player.bet = int(bet)
                except ValueError:
                    print(f'"{bet}" is an invalid entry. Use numbers only, betwee 2 and 10.')
                    continue
                if 2 <= bet <= 10:
                    try:
                        player.bet(bet)
                    except ValueError:
                        print(f"Insufficient funds, balance remaining: {player.balance}")
                        break
                else:
                    print(f'Try again, bet must be between $2 and $10.')

#Initialize players.
init_players()
game_deck = Deck()
initial_draw()