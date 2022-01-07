import random
from shutil import get_terminal_size
from os import system
from time import sleep

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
turns = 0

header = {
    # Just for me to keep track my versions.
    'title':   'War!',
    'tag1':    'Written by Maxime Langlois-Morin.',
    'tag2':    'Milestone Project 2 Warm-Up - 2022 Complete Python Bootcamp From Zero to Hero in Python by Pieran Data',
    'version': '0.0.5',
    'date':    'December 17th 2021'
            }


class Player:

    def __init__(self, name):

        self.name = name
        self.hand = None

    def play_card(self, state='normal'):
        if state == 'normal':
            if len(self.hand) > 0:
                return self.hand.pop(0)

        else:
            if len(self.hand) < 3:
                num = len(self.hand)
                return [self.hand.pop(0) for card in range(num - 1)]
            else:
                return [self.hand.pop(0) for card in range(3)]

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards.'

    def show_hand(self):
        print(f"{self.name}'s hand contains {len(self.hand)} cards, and consists of:\n")
        for card in self.hand:
            print(f'{card}')
class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

    def __int__(self):
        return self.value

class Table:

    def __init__(self):

        self.p1_pot = []
        self.p2_pot = []

    def take_cards(self, player):
        
        all_cards = []

        # a little bit of randomness to prevent games from getting stuck in infinite loops.

        if random.randint(1,100) % 2 == 0:
            all_cards = self.p1_pot + self.p2_pot
        else:
            all_cards = self.p2_pot + self.p1_pot

        if player == 'player1':
            player1.hand.extend(all_cards)
        else:
            player2.hand.extend(all_cards)
        
        self.p1_pot = []
        self.p2_pot = []

class Deck:

    def __init__(self):

        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def __len__(self):
        return(len(self.all_cards))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def draw_card(self):
        return self.all_cards.pop(0)

    def deal_cards(self):
        middle = len(self.all_cards) // 2
        return (self.all_cards[:middle], self.all_cards[middle:])

def clear_output():
    system('clear')

def draw_header():
    clear_output()
    print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()
          [0] + f'Turn #:{turns}\n\nPlayer 1\t\t\tPlayer 2\nCards remaining: {len(player1.hand)}\t\tCards remaining: {len(player2.hand)}\n\n')


def play_hand(table):

    table.p1_pot.append(player1.play_card())
    table.p2_pot.append(player2.play_card())

    if table.p1_pot[0].value > table.p2_pot[0].value:
        print(f'{table.p1_pot[0]} > {table.p2_pot[0]}, player 1 wins!')
        table.take_cards('player1')
    

    elif table.p1_pot[0].value < table.p2_pot[0].value:
        print(f'{table.p1_pot[0]} < {table.p2_pot[0]}, player 2 wins!')
        table.take_cards('player2')
        

    elif table.p1_pot[0].value == table.p2_pot[0].value:
        print(f'{table.p1_pot[0]} & {table.p2_pot[0]} values are equal. WAR!')
        war()


def war():
    war = True

    while war == True:
        tbl.p1_pot.extend(player1.play_card('war'))
        tbl.p2_pot.extend(player2.play_card('war'))

        if tbl.p1_pot[-1].value > tbl.p2_pot[-1].value:
            print(f'{tbl.p1_pot[-1]} beats {tbl.p2_pot[-1]}, player 1 wins!\n')
            print('\nPlayer 1 Pot Contains:\n')
            for card in tbl.p1_pot:
                print(card)
            print('\nPlayer 2 Pot Pot Contains:\n')
            for card in tbl.p2_pot:
                print(card)
            #sleep(0.5)
            tbl.take_cards('player1')
            war = False
            

        elif tbl.p2_pot[-1].value > tbl.p1_pot[-1].value:
            print(f'{tbl.p2_pot[-1]} beats {tbl.p1_pot[-1]}, player 2 wins!\n')
            print('\nPlayer 1 Pot Contains:\n')
            for card in tbl.p1_pot:
                print(card)
            print('\nPlayer 2 Pot Pot Contains:\n')
            for card in tbl.p2_pot:
                print(card)
            #sleep(0.5)
            tbl.take_cards('player2')
            war = False
            


if __name__ == '__main__':

    #init players and deal cards
    player1 = Player("Max")
    player2 = Player("Jose")
    tbl = Table()
    game_deck = Deck()
    game_deck.shuffle()
    player1.hand, player2.hand = game_deck.deal_cards()
    draw_header()
    while len(player1.hand) != 0 and len(player2.hand) != 0:
        play_hand(tbl)
        #sleep(0.1)
        turns += 1
        tbl = Table()
        draw_header()
    else:
        print('Game over')
        print(f'Game completed in {turns} turns.')
