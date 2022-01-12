
from random import shuffle
class Card:
    """
    Card class, is used by the Deck class to create individual card objects
    to populate a created Deck object.
    """ 
    def __init__(self, suit, rank):
        values = {
        'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
        'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
        'Ace': 11
        }
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """Creates an instance of a Deck object containing 52 instances of Card
    class by looping through the rank list for each suit in the suit list
    """
    def __init__(self):
        self.cards = []
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = (
            'Two', 'Three', 'Four', 'Five', 'Six', 'Seven','Eight', 'Nine',
            'Ten', 'Jack', 'Queen', 'King', 'Ace'
            )

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)
        
        shuffle(self.cards)


class Player:
    """
    Takes in a passed in name, and initializes a player object with a starting
    balance of $100.00, and an empty hand.
    """
    def __init__(self,name) -> str:
        self.name = name
        self.balance = 100.00
        self.hand = []
    
    def __int__(self):
        return sum(self.hand)
    
    def hand_value(self):
        value = 0
        for card in self.hand:
            value += card.value
        return value


class Dealer:
    """
    Creates a dealer class, to house the dealers hand.  Not certain this
    is 100% necessary, hand could be a variable in the main loop...
    """
    def __init__(self):
        self.hand = []
        self.name = 'the dealer'


def draw_cards(num,deck,player):
    
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

def main():
    name = input('Enter your name.\n>')
    player = Player(name)
    dealer = Dealer()
    
    while True:
        deck = Deck
        print('Dealing cards')
        draw_cards(2,deck,dealer)
        draw_cards(2,deck,player)
        print(f'Your hand contains the following cards, and has a value of
         {player.hand_value()}\n')
        for card in player.hand:
            print(card)
    


