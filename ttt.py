from copy import deepcopy
import string
from time import sleep
import random
from shutil import get_terminal_size
from os import system 


#global variables
header = {
# Just for me to keep track my versions.
            'title':   'A simple game of Tic Tac Toe',
            'tag1':    'Developed by Maxime Langlois-Morin, with no sample code or examples from bootcamp ipnyb notebook.',
            'tag2':    'Milestone Project 1 - 2022 Complete Python Bootcamp From Zero to Hero in Python by Pieran Data',
            'version': '0.0.24',
            'date':    'December 9th 2021'
            }
player1 = {
            'init':False,
            'token':'',
            'score':0,
            'player_name':'Player 1'
}

player2 = {
            'init':False,
            'token':'',
            'score':0,
            'player_name':'Player 1'
}

turn_order = {
            'first':'',
            'second':''
}

game_count = 1
board = {}
game_on = True

def clear_output():
    system('clear')

def draw_header(state):
    # Draw screen based on passed in argument.
    clear_output()

    if state == 'pre_game':
        if player1['token'] == '' and player2['token'] == '':
            print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] +'\n\n')
        elif player1['token'] != '' and player2['token'] == '':
            print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] + "\n\nPlayer 1: " + player1['token'] + '\n\n')
        else:
            print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] + "\n\nPlayer 1: " + player1['token'] + "\tPlayer 2: " + player2['token'] +"\n\n")

    elif state == 'game':
        print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] + "\n\nPlayer 1: " + player1['token'] + "\tPlayer 2: " + player2['token'] + "\nScore: " + str(player1['score']) + "\tScore: " + str(player2['score']) +"\n\n")

def init_board():
    #Set global board to initial empty state.
    return {'row1':list('   |   |   \n   |   |   \n___|___|___'),'row2':list('   |   |   \n   |   |   \n___|___|___'),'row3':list('   |   |   \n   |   |   \n   |   |   ')}

def init_players():
    global player1
    global player2
    # Initialize player token, takes in a letter.
    player1_token = ''
    player2_token = ''

    #init player 1
    while player1_token.isalpha() == False:
        draw_header('pre_game')
        print('Player 1, select a letter to use as your token. Only letters are accepted.')
        player1_token = input('').upper()
        if player1_token not in string.ascii_uppercase:
            draw_header('pre_game')
            print('Only letters from A-Z are accepted. Please try again...')

        else:
            #convert to dictionary
            d = {'token':player1_token,'init':True}
            player1.update(d)
            draw_header('pre_game')


    #init player 2
    while player2_token.isalpha() == False:
        draw_header('pre_game')
        print('Player 2, select a letter to use as your token. Only letters are accepted.')
        player2_token = input('').upper()
        if player2_token not in string.ascii_uppercase:
            draw_header('pre_game')
            print('Only letters from A-Z are accepted. Please try again...')

        else:
            player2.update({'token':player2_token,'init':True})
            draw_header('pre_game')


def coin_flip():

    global turn_order

    # Flip a coin 50 times, count number of heads and tails to determine player order.  Home is player who flips coin.
    result = []
    order = {}
    coin = ['heads','tails']
    coin_face = None

    #Determine who gets to choose coin_face

    if game_count % 2 != 0:
        flip = 'player1'
        no_flip = 'player2'
    else:
        flip = 'player2'
        no_flip = 'player1'

    draw_header('pre_game')
    print(f'{flipper}, select heads or tails')
    while coin_face == None:
        selection = input('Enter 1 for heads, 2 for tails.\n>')
        if selection == "1":
            coin_face = 0
            print(f'{coin[0]} selected!\n')
            sleep(1)
        elif selection == '2':
            coin_face = 1
            print(f'{coin[1]} selected!\n')
            sleep(1)
        else:
            print('Invalid entry')

    # Begin coin flip.
    draw_header('pre_game')
    print('Flipping coin!')
    sleep(1)

    for flip in range(1,51):
        if random.randint(1,2) == 1:
            result.append('heads')
        else:
            result.append('tails')

    if coin_face == 0:
        #Heads picked for coin_flip
        if result.count(coin[0]) > result.count(coin[1]):
            print(f'Heads!\n\n{flip} goes first!')
            turn_order = {'first':flip,'second':no_flip}
            sleep(2)
        else:
            print(f'Tails!\n\n{no_flip} goes first!')
            turn_order = {'first':no_flip,'second':flip}
            sleep(2)
    else:
        #Tails picked for coin_flip
        if result.count(coin[0]) < result.count(coin[1]):
            print(f'Heads!\n\n{no_flip} goes first!')
            turn_order =  {'first':no_flip,'second':flip}
            sleep(2)
        else:
            print(f'Tails!\n\n{flip} goes first!')
            turn_order =  {'first':flip,'second':no_flip]}
            sleep(2)

def draw_board(type='current_state'):
    #If 'current_state' state is passed in, board is drawn in its current game state. If 'play' is passed, the board is drawn with numbers to indicate to players which numbers correspond to each of 9 board locations.

    global board

    if type == "current_state":
        print(''.join(board['row1']),''.join(board['row2']),''.join(board['row3']), sep="\n")
    elif type == "play":
        lbl_board = deepcopy(board)
        lbl_board['row1'][0] = '1'
        lbl_board['row1'][4] = '2'
        lbl_board['row1'][8] = '3'
        lbl_board['row2'][0] = '4'
        lbl_board['row2'][4] = '5'
        lbl_board['row2'][8] = '6'
        lbl_board['row3'][0] = '7'
        lbl_board['row3'][4] = '8'
        lbl_board['row3'][8] = '9'
        print(''.join(lbl_board['row1']),''.join(lbl_board['row2']),''.join(lbl_board['row3']), sep="\n")

def take_turn(player_turn):
    placed = False
    # takes user input, and run check_space()
    place = ''
    while placed == False:
        print()
        place = input(f'{player_turn}, make your move.\n>')
        if place == '1':
            if board['row1'][13] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row1'][13] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row1'][13] = player2['token']
                    placed = True
        elif place == '2':
            if board['row1'][17] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row1'][17] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row1'][17] = player2['token']
                    placed = True
        elif place == '3':
            if board['row1'][21] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row1'][21] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row1'][21] = player2['token']
                    placed = True
        elif place == '4':
            if board['row2'][13] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row2'][13] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row2'][13] = player2['token']
                    placed = True
        elif place == '5':
            if board['row2'][17] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row2'][17] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row2'][17] = player2['token']
                    placed = True
        elif place == '6':
            if board['row2'][21] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row2'][21] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row2'][21] = player2['token']
                    placed = True
        elif place == '7':
            if board['row3'][13] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row3'][13] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row3'][13] = player2['token']
                    placed = True
        elif place == '8':
            if board['row3'][17] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row3'][17] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row3'][17] = player2['token']
                    placed = True
        elif place == '9':
            if board['row3'][21] != ' ':
                print('Invalid choice, cannot place token over an existing token.')
            else:
                if player_turn == 'player1':
                    board['row3'][21] = player1['token']
                    placed = True
                elif player_turn == 'player2':
                    board['row3'][21] = player2['token']
                    placed = True

def winner(player):
    #check for win condition
    if board['row1'][13] == player['token'] and board['row2'][13] == player['token'] and board['row3'][13] == player['token']:
        #Column 1
        return True
    elif board['row1'][17] == player['token'] and board['row2'][17] == player['token'] and board['row3'][17] == player['token']:
        #Column 2
        return True
    elif board['row1'][21] == player['token'] and board['row2'][21] == player['token'] and board['row3'][21] == player['token']:
        #Column 3
        return True
    elif board['row1'][13] == player['token'] and board['row1'][17] == player['token'] and board['row1'][21] == player['token']:
        #Row 1
        return True
    elif board['row2'][13] == player['token'] and board['row2'][17] == player['token'] and board['row2'][21] == player['token']:
        #Row 2
        return True
    elif board['row3'][13] == player['token'] and board['row3'][17] == player['token'] and board['row3'][21] == player['token']:
        #Row 3
        return True
    elif board['row1'][13] == player['token'] and board['row2'][17] == player['token'] and board['row3'][21] == player['token']:
        #Diagonal \
        return True
    elif board['row1'][21] == player['token'] and board['row2'][17] == player['token'] and board['row3'][17] == player['token']:
        #Diagonal /
        return True
    else:
        return False

def play_game():
    # Game variables
    player_turn = ''
    turn = 0

    # Check who's playing next
    def check_turn():
        #binding to parent player_turn
        nonlocal player_turn
        # If turn = 0 or turn is even, first person in turn_order plays.  If turn is odd, second person in turn_order plays.
        if turn == 0 or turn % 2 == 0:
            player_turn = turn_order['first']
        else:
            player_turn = turn_order['second']

    draw_header('pre_game')
    input('Press Enter when ready to start!')
# Determine who plays first.
    coin_flip()

# Loop through game, start checking for wins after 3 turns, and continue until winner or 9 turns have been played.
    while turn < 9:
        if turn <= 2:
            check_turn()
            draw_header('game')
            draw_board('play')
            take_turn(player_turn)
            turn += 1
        if turn >= 3:
            check_turn()
            print(player_turn)
            draw_header('game')
            draw_board('play')
            take_turn(player_turn)
            # When 3rd turn is taken (and each subsequent turn after), check if there is a winner.
            if winner(player_turn):
                game_over(player_turn)
            turn += 1
    if turn == 9:
        check_turn()
        draw_header('game')
        draw_board('play')
        take_turn(player_turn)

        if winner(player_turn):
            game_over(player_turn)
        else:
            game_over('stalemate')

def game_over(state):
    global game_on
    global player1
    global player2
    if state == 'stalemate':
        draw_header('game')
        draw_board()
        print('Stalemate!')
        game_on = keep_playing()

    else:
        draw_header(game)
        draw_board()
        print(f'{state["player_name"]} wins!')
        state['score'] += 1
        game_on = keep_playing()

def keep_playing():
    draw_header()
    response = input('Play again?\n(Y)es or (N)o\n>').lower
    while 'y' or 'n' not in response:
        if 'y' in response.lower():
            return True
        elif 'n' in response.lower():
            return False
        else:
            print('Invalid response, please enter (Y)es or (N)o')

def main_loop():
    global board
    while game_on == True:
        draw_header('pre_game')
        # Set initial board state
        board = init_board()
        #Initialize player token on first playthrough.  Token is the letter player is using for their game piece.
        if player1['init'] == False & player2['init'] == False:
            init_players()
        play_game()

main_loop()
