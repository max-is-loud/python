from os import name, system
from shutil import get_terminal_size
from time import sleep

from classes import *

# Global Variables
players = {"dealer": Player("dealer")}  # Initialize players dict with dealer.
min_bet = 2
max_bet = 50
lines = 0  # counts how many printed lines between draw_screen() calls.
turns = 0


def b_align(x, y=0):
    """
    Facilitates prints on the bottom of the terminal, by taking in x as the current
    number of rows printed since last screen draw (lines) and y - number of
    lines in print statement and returning the appropriate number of new lines.
    """
    return "\n" * (get_terminal_size()[1] - (x + y))


def draw_screen(mode="no_hand", player=None):
    global lines
    header = {
        # Just for me to keep track my versions.
        "title": "Blackjack",
        "tag1": "Written by Maxime Langlois-Morin.",
        "tag2": "Milestone Project 2 - 2022 Complete Python Bootcamp From Zero to Hero in Python by Pieran Data",
        "date": "February 1st 2022 - Ver 0.3",
    }

    def clear_console():
        command = "clear"
        if name in ("nt", "dos"):  # If machine is running Windows, use cls
            command = "cls"
        system(command)

    def print_header():
        global lines
        for value in header.values():
            print(value)
            lines += 1
        print("-" * get_terminal_size()[0])
        lines += 1

    def print_money(player=None):
        global lines

        player_list = []
        player_balances = []
        player_bets = []
        for i, x in enumerate(players.values()):
            if x.name == "Dealer":
                continue
            else:
                player_list.append(x.name)
                player_balances.append(x.balance)
                player_bets.append(x.bet)
        print(f'{"Player":<10}{"Balance":^10}{"Bet":^10}{"Status":<10}')
        lines += 1
        for i, x in enumerate(player_list):
            if i == 0:
                continue

            if player == None or player == 'dealer':
                print(
                    f"{player_list[i]:<10}{'$' + str(player_balances[i]):^10}{'$' + str(player_bets[i]):^10}{'Waiting':<10}"
                )
                lines += 1
            elif x == player.name:
                print(
                    f"{player_list[i]:<10}{'$' + str(player_balances[i]):^10}{'$' + str(player_bets[i]):^10}{'Playing':<10}"
                )
                lines += 1
            elif players[f"player_{i}"].stand == True:
                print(
                    f"{player_list[i]:<10}{'$' + str(player_balances[i]):^10}{'$' + str(player_bets[i]):^10}{'Stand':<10}"
                )
                lines += 1
            elif players[f"player_{i}"].blackjack == True:
                print(
                    f"{player_list[i]:<10}{'$' + str(player_balances[i]):^10}{'$' + str(player_bets[i]):^10}{'Blackjack!':<10}"
                )
                lines += 1
            elif players[f"player_{i}"].bust == True:
                print(
                    f"{player_list[i]:<10}{'$' + str(player_balances[i]):^10}{'$' + str(player_bets[i]):^10}{'Bust!':<10}"
                )
                lines += 1
            else:
                print(
                    f"{player_list[i]:<10}{'$' + str(player_balances[i]):^10}{'$' + str(player_bets[i]):^10}{'Waiting':<10}"
                )
                lines += 1
        print("-" * get_terminal_size()[0])
        lines += 1

    def print_draw():
        global lines
        for x in range(1, len(players)):
            print(
                f'{players[f"player_{x}"].name}: {players[f"player_{x}"].show_hand()}\n'
            )
            lines += 2
        if len(players["dealer"].hand) > 0:
            print(f'Dealer\'s face up card: {players["dealer"].hand[0]}')
            lines += 1

    def print_naturals():
        for x in range(1, len(players)):
            if players[f"player_{x}"].blackjack == True:
                print(f'{b_align(lines)}{players[f"player_{x}"].name}, Blackjack!')
        input(f"{b_align(lines)}Press enter to continue...")

    def print_hand(player="dealer"):
        global lines

        if player == "dealer":
            for x in range(1, len(players)):
                if players[f"player_{x}"].stand == True:
                    print(
                        f"Player {x}: {players[f'player_{x}'].name} - Stand\n{players[f'player_{x}'].show_hand()} - {players[f'player_{x}'].hand_value()}\n"
                    )
                    lines += 3
                elif players[f"player_{x}"].blackjack == True:
                    print(
                        f"Player {x}: {players[f'player_{x}'].name} - Blackjack!\n{players[f'player_{x}'].show_hand()} - {players[f'player_{x}'].hand_value()}\n"
                    )
                    lines += 3
                elif players[f"player_{x}"].bust == True:
                    print(
                        f"Player {x}: {players[f'player_{x}'].name} - Bust!\n{players[f'player_{x}'].show_hand()} - {players[f'player_{x}'].hand_value()}\n"
                    )
                    lines += 3
                else:
                    print(
                        f"Player {x}: {players[f'player_{x}'].name} - waiting\n{players[f'player_{x}'].show_hand()} - {players[f'player_{x}'].hand_value()}\n"
                    )
                    lines += 3

        else:
            for x in range(1, len(players)):
                if players[f"player_{x}"].stand == True:
                    print(
                        f"Player {x}: {players[f'player_{x}'].name} - Stand\n{players[f'player_{x}'].show_hand()} - {players[f'player_{x}'].hand_value()}\n"
                    )
                    lines += 3
                elif players[f"player_{x}"].blackjack == True:
                    print(
                        f"Player {x}: {players[f'player_{x}'].name} - Blackjack!\n{players[f'player_{x}'].show_hand()} - {players[f'player_{x}'].hand_value()}\n"
                    )
                    lines += 3
                elif players[f"player_{x}"].bust == True:
                    print(
                        f"Player {x}: {players[f'player_{x}'].name} - Bust!\n{players[f'player_{x}'].show_hand()} - {players[f'player_{x}'].hand_value()}\n"
                    )
                    lines += 3
                else:
                    if player is players[f"player_{x}"]:
                        print(f"Player {x}: {players[f'player_{x}'].name} - Playing\n")
                        lines += 2
                    else:
                        print(
                            f"Player {x}: {players[f'player_{x}'].name} - waiting\n{players[f'player_{x}'].show_hand()} - {players[f'player_{x}'].hand_value()}\n"
                        )
                        lines += 3
                
        print("\n" * (get_terminal_size()[1] - 33))
        lines += get_terminal_size()[1] - 32

        if player == "dealer":
            print("Dealer's turn...\n")
            lines += 2
            print(f'Dealer:\n {players["dealer"].hand[0]}\n')
        else:
            print(f"{player.name} is playing.\n")
            lines += 2
            print(f'Dealer:\n{players["dealer"].hand[0]}\n')
            lines += 2
            print(
                f"{player.name}\nCurrent hand: {player.show_hand()}\nHand Values:{player.hand_value()}\n"
            )
            lines += 4

    def print_dpeek():
        global lines
        print("Dealer checks his hand...")
        lines += 1
        for x in range(5):
            print(".")
            lines += 1
            sleep(0.3)
        if players["dealer"].blackjack == True:
            print(f"... and reveals a Blackjack!\n{players['dealer'].show_hand()}")
            lines += 1
        else:
            print("... play continues.")
            lines += 1

    def print_settle():
        global lines
        if players["dealer"].blackjack == True:
            for x in range(1, len(players)):
                if players[f"player_{x}"].blackjack == True:
                    print(
                        f'{players[f"player_{x}"].name} ties with the dealer. Bet of ${players[f"player_{x}"].bet} returned.\nBalance: ${players[f"player_{x}"].balance}\n'
                    )
                    lines += 3
                elif players[f"player_{x}"].blackjack == False:
                    print(
                        f'{players[f"player_{x}"].name}\'s hand loses. Bet of ${players[f"player_{x}"].bet} lost.\nBalance: ${players[f"player_{x}"].balance}\n'
                    )
                    lines += 3
        elif players["dealer"].bust == True:
            for x in range(1, len(players)):
                if players[f"player_{x}"].bust != True:
                    print(
                        f'{players[f"player_{x}"].name}\'s hand wins! {players[f"player_{x}"].bet * 2} paid.\nBalance: ${players[f"player_{x}"].balance}\n'
                    )
                    lines += 3
                else:
                    print(
                        f'{players[f"player_{x}"].name} busted. Bet of ${players[f"player_{x}"].bet} lost.\nBalance: ${players[f"player_{x}"].balance}\n'
                    )
                    lines += 3
        elif players["dealer"].stand == True:
            for x in range(1, len(players)):
                if players[f"player_{x}"].hand_value() > players["dealer"].hand_value():
                    if players[f"player_{x}"].bust == True:
                        print(
                            f'{players[f"player_{x}"].name}\'s hand loses. Bet of ${players[f"player_{x}"].bet} lost.\nBalance: ${players[f"player_{x}"].balance}\n'
                        )
                        lines += 3
                    else:
                        print(
                            f'{players[f"player_{x}"].name}\'s hand wins! {players[f"player_{x}"].bet * 2} paid.\nBalance: ${players[f"player_{x}"].balance}\n'
                        )
                        
                elif (
                    players[f"player_{x}"].hand_value()
                    == players["dealer"].hand_value()
                ):
                    print(
                        f'{players[f"player_{x}"].name} ties with the dealer. Bet of ${players[f"player_{x}"].bet} returned\nBalance: ${players[f"player_{x}"].balance}\n'
                    )
                    lines += 3
                elif (
                    players[f"player_{x}"].hand_value() < players["dealer"].hand_value()
                ):
                    print(
                        f'{players[f"player_{x}"].name}\'s hand loses. Bet of ${players[f"player_{x}"].bet} lost.\nBalance: ${players[f"player_{x}"].balance}\n'
                    )
                    lines += 3

    def print_dealer_turn():
        global lines
        print("Dealer's turn...\n")
        lines += 2
        print(f'Dealer:\n {players["dealer"].show_hand()} - {players["dealer"].hand_value()}\n')
        lines += 3
            


    clear_console()
    print(lines)
    lines = 0  # reset printed lines counter
    if mode == "no_hand":
        print_header()

    if mode == "place_bet":
        print_header()
        print_money()

    if mode == "draw":
        print_header()
        print_money()
        print_draw()

    if mode == "hand_dpeek":
        print_header()
        print_money()
        print_dpeek()

    if mode == "settle":
        print_header()
        print_settle()

    if mode == "play":
        print_header()
        print_money(player)
        print_hand(player)

    if mode == "new_hand":
        print_header()
        print_money()

    if mode == "print_naturals":
        print_header()
        print_money()
        print_naturals()

    if mode == "dealers_turn":
        print_header()
        print_money()
        print_dealer_turn()


def init_players():
    """Initializes players, based in user input."""
    global players
    global lines
    global turns
    names = []
    balance = None

    if turns == 0:

        while True:
            draw_screen()
            num = input(
                f"{b_align(lines,2)}How many players? Enter a number between 1 and 6\n>"
            )
            try:
                num = int(num)
            except ValueError:
                draw_screen()
                input(
                    f"{b_align(lines,1)}Invalid entry, a number between 1 and 6 only. Press enter to continue"
                )
                continue
            if 1 <= num <= 6:
                break
            else:
                draw_screen()
                input(
                    f"{b_align(lines,1)}6 players maximum only. Press enter to continue."
                )
                sleep(2)
        draw_screen()
        print(f"{num} players playing!")
        lines += 1
        for x in range(1, num + 1):
            draw_screen()
            names.append(input(f"{b_align(lines,2)}Player {x}, enter your name:\n>"))

        while True:
            draw_screen()
            balance = input(
                f"{b_align(lines,2)}Enter a starting balance amount between $100 and $1000\n>"
            )

            try:
                balance = int(balance)
            except ValueError:
                draw_screen()
                input(
                    f"{b_align(lines,2)}Invalid entry, a number between $100 and $1000 only.\nPress Enter to continue."
                )
                continue
            if 100 <= balance <= 10000:
                break
            else:
                draw_screen()
                input(
                    f"{b_align(lines,2)}Invalid entry, a number between $100 and $1000 only.\nPress Enter to continue."
                )

        for p, name in enumerate(names, start=1):
            players[f"player_{p}"] = Player(name, balance)

    else:
        for player in players.values():
            player.status = None
            player.bust = False
            player.blackjack = False
            player.stand = False


def place_bets():
    for x in range(1, len(players)):
        if players[f"player_{x}"].balance < 2:
            continue
        else:
            while True:
                draw_screen("place_bet")
                bet = input(
                    f'{b_align(lines,2)}Player: {players[f"player_{x}"].name}, place your bet (Bets must be between ${min_bet} and ${max_bet})\n>'
                )
                # 1`if input is a number.
                try:
                    bet = int(bet)
                    assert (
                        min_bet <= bet <= max_bet
                    ), f"{b_align(lines,1)}Bet amount: ${bet} is invalid. Bets must be between: ${min_bet} & ${max_bet}"

                except ValueError:
                    print("Invalid entry")

                except AssertionError as err:
                    print(err)

                # check if bet is within allowed amounts, if true, place bet.

                else:
                    try:
                        players[f"player_{x}"].bet = bet
                    except ValueError:
                        print("Insufficient Balance")
                    else:
                        break
        if x == (len(players) - 1):
            draw_screen("place_bet")
            input(f"{b_align(lines,1)}Press enter to continue...")
        else:
            draw_screen("place_bet")


def initial_draw():
    """Runs through the process of dealing initial cards to all players.
    Deals 1 card to player 1 through to the last player, then one to the dealer.
    Repeats process again from player 1 onwards for second card.

    For loop below calls range with the stop number being the length of the
    player list, which is exclusive of the last number - which is fine because
    dealer is ignored.
    """
    # Delete old hands.
    del players["dealer"].hand
    for x in range(1, len(players)):
        del players[f"player_{x}"].hand

    draw_screen("draw")
    input(f"{b_align(lines, 1)}Press enter to continue...")

    while len(players["dealer"].hand) < 2:
        for x in range(1, len(players)):
            players[f"player_{x}"].hand = game_deck.draw_card()
            draw_screen("draw")
            sleep(0.5)
        players["dealer"].hand = game_deck.draw_card()
        draw_screen("draw")
        sleep(0.5)
    input(f"{b_align(lines,1)}Press enter to continue...")
    # check if any players have a natural 21. If yes, set Player.blackjack to True
    naturals = 0
    for x in range(1, len(players)):
        if players[f"player_{x}"].hand_value() == 21:
            players[f"player_{x}"].blackjack == True
            naturals += 1
    if naturals >= 1:
        draw_screen("print_naturals")


def play_hand():
    
    # If player already has Blackjack, has stood, or is bust and skip them
    for x in range(1, len(players)):
        if (
            players[f"player_{x}"].blackjack == True
            or players[f"player_{x}"].stand == True
            or players[f"player_{x}"].bust == True
        ):
            continue
        else:
            """
            Player turn.  Loops through showing cards, prompting
            player to hit and stand, and repeats until player either
            stands, busts or gets a blackjack.
            """
            play = True
            while play:
                choice = ""
                while True:
                    draw_screen("play", players[f"player_{x}"])
                    choice = input(
                        f"{b_align(lines,5)}Make a selection:\n\n1: Hit\n2: Stand\n"
                    )
                    if choice == "1":
                        players[f"player_{x}"].hand = game_deck.draw_card()
                        if players[f"player_{x}"].hand_value() > 21:
                            players[f"player_{x}"].bust = True
                            draw_screen("play", players[f"player_{x}"])
                            print(
                                f'Bust!\n{players[f"player_{x}"].name} has {players[f"player_{x}"].hand_value()}!'
                            )
                            input("Press enter to continue...")
                            play = False
                            break
                        elif players[f"player_{x}"].hand_value() == 21:
                            players[f"player_{x}"].blackjack = True
                            draw_screen("play", players[f"player_{x}"])
                            print(
                                f'{b_align(lines,1)}Blackjack!\n{players[f"player_{x}"].name} has {players[f"player_{x}"].hand_value()}!'
                            )
                            input("Press enter to continue...")
                            play = False
                            break
                        else:
                            continue
                    elif choice == "2":
                        players[f"player_{x}"].stand = True
                        play = False
                        break
                    else:
                        print("Invalid selection")

                if players[f"player_{x}"].hand_value() < 21:
                    print(
                        f'{players[f"player_{x}"].name} stood at {players[f"player_{x}"].hand_value()}.'
                    )
                    print("Press enter to continue...")
                break

def dealer_check():
    global players
    if players["dealer"].hand_value() == 21:
        players["dealer"].blackjack = True
        draw_screen("hand_dpeek")
        input(f"{b_align(lines +1)}Press enter to continue...")
        return True
    else: 
        draw_screen("hand_dpeek")
        input(f"{b_align(lines + 1)}Press enter to continue...")
        return False


def dealer_turn():
    global players

    draw_screen("dealers_turn")
    print(
        f'Dealer reveal:\n{players["dealer"].show_hand()} - {players["dealer"].hand_value()}'
    )
    input("Press enter to continue...")
    while True:
        
        if players["dealer"].hand_value() < 17:
            players["dealer"].hand = game_deck.draw_card()
            draw_screen("dealers_turn")
            input(f"{b_align(lines)}Press enter to continue...")
        elif 17 < players["dealer"].hand_value() < 21:
            players["dealer"].stand = True
            draw_screen("dealers_turn")
            input(f"{b_align(lines)}Press enter to continue...")
            break
        elif players["dealer"].hand_value() == 21:
            print(f'{players["dealer"].show_hand()} - {players["dealer"].hand_value()}')
            players["dealer"].blackjack = True
            draw_screen("dealers_turn")
            input(f"{b_align(lines)}Press enter to continue...")
            break
        else:
            players["dealer"].bust = True
            draw_screen("dealers_turn")
            input(f"{b_align(lines)}Press enter to continue...")
            break


def settle():
    """
    Calculates player score, and pays out winnings or collects bet as needed.

    Scenario 1: Dealer has a natural 21.
    Action: Return the bets of any player that also has a natural 21. Collect
    the bets of any player with less than 21.

    Scenario 2: Dealer busts.
    Action: Pay the bets of any players that have stood at less than 21 (or
    have a Blackjack).  Collect the bets of any players who have also busted.

    Scenario 3: Dealer stands with >= 17 and < 21.
    Action 1: Pay out the bets of any players who stood with a hand value greater
    than the value of the dealers hand.
    Action 2: Collect the bets of players with a hand value less than that of
    the dealer.
    Action 3: Return the bet of any player who's hand is equal to that of the
    dealer's
    """
    if players["dealer"].blackjack == True:
        for x in range(1, len(players)):
            if players[f"player_{x}"].blackjack == True:
                players[f"player_{x}"].return_bet()
                draw_screen("settle")

            else:
                draw_screen("settle")

    elif players["dealer"].bust == True:
        for x in range(1, len(players)):
            if players[f"player_{x}"].bust == True:
                draw_screen("settle")

            else:
                players[f"player_{x}"].balance_add(players[f"player_{x}"].bet * 2)
                draw_screen("settle")

    elif players["dealer"].stand == True:
        for x in range(1, len(players)):
            if players[f"player_{x}"].hand_value() > players["dealer"].hand_value():
                if players[f"player_{x}"].bust == True:
                    draw_screen("settle")

                else:
                    players[f"player_{x}"].balance_add(players[f"player_{x}"].bet * 2)
                    draw_screen("settle")

            elif players[f"player_{x}"].hand_value() == players["dealer"].hand_value():
                players[f"player_{x}"].return_bet()
                draw_screen("settle")

            elif players[f"player_{x}"].hand_value() < players["dealer"].hand_value():
                draw_screen("settle")

    for x in range(1, len(players)):
        del players[f"player_{x}"].bet
    input(f"{b_align(lines, 1)}Press enter to continue...")


def check_balances(): 
    if len(players) == 1:
        draw_screen()
        print(f"{b_align(lines)}All players eliminted.  Good bye!")
        quit()
    else:
        return

def eliminate():
    global players
    new_players = {}
    counter = 0
    for key, value in players.items():
        if key == 'dealer':
            new_players['dealer'] = players['dealer']
            counter += 1
        elif value.balance < min_bet:
            continue
        else:
            new_players[f'player_{counter}'] = players[key]
            counter += 1
    return new_players


def main():
    global players
    global lines
    global turns
    global game_deck
    game_deck = Deck()
    while True:
        init_players()
        place_bets()
        initial_draw()
        if dealer_check():
            settle()
            players = eliminate()
            check_balances()
            turns += 1
        else:
            play_hand()
            # Dealer's turn.
            dealer_turn()
            settle()
            players = eliminate()
            check_balances()
            turns += 1


main()
