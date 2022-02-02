from random import shuffle

class Card:
    """
    Card class, is used by the Deck class to create individual card objects
    to populate a created Deck object.
    """

    def __init__(self, suit, rank):
        values = {
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
            "Seven": 7,
            "Eight": 8,
            "Nine": 9,
            "Ten": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            "Ace": 11,
        }
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        if self.face_up == True:
            return self.rank + " of " + self.suit
        else:
            return "*****"


class Deck:
    """Creates an instance of a Deck object containing 52 instances of Card
    class by looping through the rank list for each suit in the suit list
    """

    def __init__(self):
        self.cards = []
        suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        ranks = (
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Jack",
            "Queen",
            "King",
            "Ace",
        )

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

        shuffle(self.cards)

    def draw_card(self, face_up=True):
        if len(self.cards) == 0:
            for suit in suits:
                for rank in ranks:
                    new_card = Card(suit, rank)
                    self.cards.append(new_card)
            shuffle(self.cards)
            return self.cards.pop()    
        else:
            return self.cards.pop()


class Player:
    """
    Takes in a passed in name, and initializes a player object with a starting
    balance of $100.00, and an empty hand.
    """

    def __init__(self, name, balance=0):
        self.name = name
        self.stand = False
        self.bust = False
        self.blackjack = False
        self.status = None
        self._bet = 0
        self._balance = balance
        self._hand = []
    
    def reveal(self):
        for card in self._hand:
            if card.face_up == False:
                card.face_up == True

    def show_hand(self):
        hand_list = []
        for card in self._hand:
            hand_list.append(str(card))
        return ", ".join(hand_list)

    def hand_value(self):
        value = 0
        ace = False
        for card in self._hand:
            if card.rank == 'Ace':
                ace = True
            value += card.value
        if value > 21 and ace == True:
                value -= 10
        return value

    def balance_add(self, amount):
        self._balance += amount

    def return_bet(self):
        self._balance += self._bet

    def __str__(self):
        pass

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
        self._hand = []

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
        self._bet = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    @balance.deleter
    def balance(self):
        del self._balance
