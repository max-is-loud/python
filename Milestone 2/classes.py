from random import shuffle

class Card:
    """
    Card class, is used by the Deck class to create individual card objects
    to populate a created Deck object.
    """ 
    def __init__(self, suit, rank) -> None:
        values = {
        'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
        'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
        'Ace': 11
        }
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit


class Deck:
    """Creates an instance of a Deck object containing 52 instances of Card
    class by looping through the rank list for each suit in the suit list
    """
    def __init__(self) -> None:
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
    def __init__(self,name) -> None:
        self.name = name
        if self.name != 'dealer':
            self.balance = 100.00
        self.hand = []
        self.stand = False
        self.bet = None
    
    def __int__(self) -> list:
        return sum(self.hand)
    
    def hand_value(self) -> int:
        value = 0
        for card in self.hand:
            value += card.value
        return value