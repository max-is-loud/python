class InsufficientBalanceError(Exception):
    """Exception raised if a player bet exceeds available balance

    Attributes:
        bet -- bet ammount supplied by player
        balance -- players remaining balance
        message -- explanation of the error
    """
    def __init__(self, bet, balance, message="You have insufficient funds in your balance."):
        self.bet = bet
        self.balance = balance
        self.message = message
        super().__init__(self.message)