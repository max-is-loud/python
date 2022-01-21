from shutil import get_terminal_size
from os import system
from time import sleep
from xmlrpc.client import Boolean
from classes import *

# Global Variables
players = {'dealer':Player('dealer')} #Initialize players dict with dealer.

def clear_output():
    system('clear')

def draw_header():
    header = {
    # Just for me to keep track my versions.
    'title':   'Blackjack',
    'tag1':    'Written by Maxime Langlois-Morin.',
    'tag2':    'Milestone Project 2 - 2022 Complete Python Bootcamp From Zero to Hero in Python by Pieran Data',
    'version': '0.0.1',
    'date':    'January 14th 2022'
    }
    clear_output()
    print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] +"\n\n\n\n\n")

def init_players():
    """Initializes players, based in user input."""
    global players
    balance = None

    while True:
        clear_output()
        draw_header()
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
        clear_output()
        draw_header()
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
        clear_output()
        draw_header()
        players[f'player_{x}'] = Player(input(f'Player {x}, enter your name:\n>'),balance)
    clear_output()
    draw_header()
    print(f'{num} players playing!')

def place_bets():
    for player in players:
        if players[player].balance < 2:
            continue
        else:
            bet = None
            while True:
                print('\n')
                bet = int(input(f'Player: {players[player].name}, place your bet\n(Bets must be between $2 and $10)\n>'))
                try:
                    players[player].bet = bet
                except ValueError:
                    print(f'"{bet}" is an invalid entry. Use numbers only, betwee 2 and 10.')
                    continue
                if 2 <= bet <= 10:
                    try:
                        players[player].bet(bet)
                    except ValueError:
                        print(f"Insufficient funds, balance remaining: {players[player].balance}")
                        break
                    finally:
                        break
                else:
                    print(f'Try again, bet must be between $2 and $10.')

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
        input("Press enter when you're ready!")
        clear_output()
        draw_header()
        print('Dealing cards')
        sleep(1)
        while cards_dealt < 2:
            for x in range(1,len(players)):
                players[f'player_{x}'].hand = game_deck.draw_card()
            players['dealer'].hand = game_deck.draw_card()
            if cards_dealt == 0:
            cards_dealt += 1
        
        #check if any players have a natural 21. If yes, set Player.blackjack to True
        for x in range(1,len(players)):
            if players[f'player_{x}'].hand_value() == 21:
                players[f'player_{x}'].blackjack = True
                print(f'Blackjack! {players[f"player_{x}"].name}')
    else: 
        players.hand = game_deck.draw_card()

def test_card(value):
    return Card('Hearts',value)

def play_hand():
    
    #Check if the dealer has a natural 21 at the start of play.
    if players['dealer'].hand_value() == 21:
        pass # call as of yet unwritten settle function to calculate post hand winnings.
    
    for x in range(1,len(players)):
        if players[f'player_{x}'].blackjack == True or players[f'player_{x}'].stand == True or players[f'player_{x}'].bust == True : #If player already has Blackjack, has stood, or is bust and skip them
            continue
        else:
            while True:
                choice = ''
                print(f'Current hand: {", ".join(players[f"player_{x}"].hand)}\nHand Values:{players[f"player_{x}"].hand_value()}\n')
                while True:
                choice = input('Make a selection:\n\n1: Hit\n2: Stand')
                try:
                    choice = int(choice)
                except ValueError:
                    print('Invalid entry.')
                    continue
                if choice == 1:
                    
                
                
                
#Initialize players.
draw_header()
init_players()
game_deck = Deck()
place_bets()
for player in players.values():
    print(f'{player.name}:\nBet: ${player.bet}\nRemaining: ${player.balance}')
initial_draw()

