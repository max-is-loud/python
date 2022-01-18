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

    def draw_card(self) -> Card:
        return self.cards.pop()


class Player:
    """
    Takes in a passed in name, and initializes a player object with a starting
    balance of $100.00, and an empty hand.
    """
    def __init__(self, name, balance=0) -> None:
        self.name = name
        self.stand = False
        self.bust = False
        self.blackjack = False
        self._bet = None
        self._balance = balance
        self._hand = []
    
    def show_hand(self) -> str:
        hand_list = []
        for card in self._hand:
            hand_list.append(str(card))
        return ', '.join(hand_list)
    
    def hand_value(self) -> int:
        self.value = 0
        for card in self._hand:
            if card.value == 11:
                if (self.value + card.value) > 21:
                    self.value += 11
                else:
                    self.value += 1
            else:
                self.value += card.value
        return self.value
        
    def __str__(self):
        cards_list = [str(card) for card in self._hand]
        return ', '.self._hand.join()
        

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, card):
        self._hand.append(card)

    @hand.getter
    def hand(self):
        return self._hand
    
    @hand.deleter
    def hand(self):
        del self._hand

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, amount):
        """If bet is greater than player balance, an error is thrown"""
        if amount > self._balance:
            raise ValueError("Insufficient Balance")
        
        self._balance = self.balance - amount
        self._bet = amount

    @bet.deleter
    def bet(self):
        del self._bet

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    @balance.deleter
    def balance(self):
        del self._balance