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
            'tag1':    'Written by Maxime Langlois-Morin.',
            'tag2':    'Milestone Project 1 - 2022 Complete Python Bootcamp From Zero to Hero in Python by Pieran Data',
            'version': '0.0.30',
            'date':    'December 10th 2021'
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

turn = 0
game_count = 1
game = True
board = {}
game_on = True
player_turn = ''


def clear_output():
    system('clear')

def draw_header(state):
    # Draw screen based on passed in argument.
    clear_output()

    if state == 'pre_game':
        if player1['token'] == '' and player2['token'] == '':
            print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] +'\n\n')
        elif player1['token'] != '' and player2['token'] == '':
            print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] + "\nPlayer 1: " + player1['token'] + '\n\n')
        else:
            print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] + "\nPlayer 1: " + player1['token'] + "\tPlayer 2: " + player2['token'] +"\n\n")

    elif state == 'game':
        print(f"{header['title']}\n{header['tag1']}\n{header['tag2']}\n{header['version']} - {header['date']}\n" + "-" * get_terminal_size()[0] + "\nPlayer 1: " + player1['token'] + "\tPlayer 2: " + player2['token'] + "\nScore: " + str(player1['score']) + "\tScore: " + str(player2['score']) +"\n\n")

def init_board():
    global board
    #Set global board to initial empty state.
    board = {'row1':list('   |   |   \n   |   |   \n___|___|___'),'row2':list('   |   |   \n   |   |   \n___|___|___'),'row3':list('   |   |   \n   |   |   \n   |   |   ')}

def init_players():

    global player1
    global player2

    # Initialize player token, takes in a letter.
    player1_token = ''
    player2_token = ''

    #init player 1
    while player1_token.isalpha() == False:
        draw_header('pre_game')
        player1_token = input('Player 1, select a letter to use as your token. Only letters are accepted.\n>').upper()

        while player1_token.isalpha() == False:
            print('Only letters from A-Z are accepted. Please try again...')
            player1_token = input('>').upper()

        else:
            player1.update({'token':player1_token,'init':True})

    #init player 2
    while player2_token.isalpha() == False:
        draw_header('pre_game')
        player2_token = input('Player 2, select a letter to use as your token. Only letters are accepted.\n>').upper()
        while player2_token.isalpha() == False:
            print('Only letters from A-Z are accepted. Please try again...')
            player2_token = input('>').upper()

        else:
            player2.update({'token':player2_token,'init':True})

def coin_flip():
    global player1
    global player2
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
    if flip == 'player1':
        print('Player 1, select heads or tails\n')
    else:
        print('Player 2, sekect heads or tails\n')
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

    for flips in range(1,51):
        if random.randint(1,2) == 1:
            result.append('heads')
        else:
            result.append('tails')

    if coin_face == 0:
        #Heads picked for coin_flip
        if result.count(coin[0]) > result.count(coin[1]):
            if flip == 'player1':
                print(f'Heads!\n\nPlayer 1 goes first!')
            else:
                print(f'Heads!\n\nPlayer 2 goes first!')
            turn_order = {'first':flip,'second':no_flip}
            sleep(2)
        else:
            if flip == 'player1':
                print(f'Tails!\n\nPlayer 2 goes first!')
            else:
                print(f'Tails!\n\nPlayer 1 goes first!')
            turn_order = {'first':no_flip,'second':flip}
            sleep(2)
    else:
        #Tails picked for coin_flip
        if result.count(coin[0]) < result.count(coin[1]):
            if flip == 'player1':
                print(f'Tails!\n\nPlayer 1 goes first!')
            else:
                print(f'Tails!\n\nPlayer 2 goes first!')
            turn_order = {'first':flip,'second':no_flip}
            sleep(2)
        else:
            if flip == 'player1':
                print(f'Heads!!\n\nPlayer 2 goes first!')
            else:
                print(f'Tails!\n\nPlayer 1 goes first!')
            turn_order =  {'first':no_flip,'second':flip}
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
        if player_turn == 'player1':
            place = input('Player 1, make your move.\n>')
        else:
            place = input('Player 2, make your move.\n>')
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

def winner(player_turn):
    #check for win condition
    if player_turn == "player1":
        if board['row1'][13] == player1['token'] and board['row2'][13] == player1['token'] and board['row3'][13] == player1['token']:
            #Column 1
            return True
        elif board['row1'][17] == player1['token'] and board['row2'][17] == player1['token'] and board['row3'][17] == player1['token']:
            #Column 2
            return True
        elif board['row1'][21] == player1['token'] and board['row2'][21] == player1['token'] and board['row3'][21] == player1['token']:
            #Column 3
            return True
        elif board['row1'][13] == player1['token'] and board['row1'][17] == player1['token'] and board['row1'][21] == player1['token']:
            #Row 1
            return True
        elif board['row2'][13] == player1['token'] and board['row2'][17] == player1['token'] and board['row2'][21] == player1['token']:
            #Row 2
            return True
        elif board['row3'][13] == player1['token'] and board['row3'][17] == player1['token'] and board['row3'][21] == player1['token']:
            #Row 3
            return True
        elif board['row1'][13] == player1['token'] and board['row2'][17] == player1['token'] and board['row3'][21] == player1['token']:
            #Diagonal \
            return True
        elif board['row1'][21] == player1['token'] and board['row2'][17] == player1['token'] and board['row3'][17] == player1['token']:
            #Diagonal /
            return True
        else:
            return False
    else:
        if board['row1'][13] == player2['token'] and board['row2'][13] == player2['token'] and board['row3'][13] == player2['token']:
            #Column 1
            return True
        elif board['row1'][17] == player2['token'] and board['row2'][17] == player2['token'] and board['row3'][17] == player2['token']:
            #Column 2
            return True
        elif board['row1'][21] == player2['token'] and board['row2'][21] == player2['token'] and board['row3'][21] == player2['token']:
            #Column 3
            return True
        elif board['row1'][13] == player2['token'] and board['row1'][17] == player2['token'] and board['row1'][21] == player2['token']:
            #Row 1
            return True
        elif board['row2'][13] == player2['token'] and board['row2'][17] == player2['token'] and board['row2'][21] == player2['token']:
            #Row 2
            return True
        elif board['row3'][13] == player2['token'] and board['row3'][17] == player2['token'] and board['row3'][21] == player2['token']:
            #Row 3
            return True
        elif board['row1'][13] == player2['token'] and board['row2'][17] == player2['token'] and board['row3'][21] == player2['token']:
            #Diagonal \
            return True
        elif board['row1'][21] == player2['token'] and board['row2'][17] == player2['token'] and board['row3'][17] == player2['token']:
            #Diagonal /
            return True
        else:
            return False

def game_over(state):

    global player1
    global player2

    if state == 'stalemate':
        draw_header('game')
        draw_board()
        print('Stalemate!')
        sleep(2)
        keep_playing()

    elif state == 'player1':
        player1['score'] += 1
        draw_header('game')
        draw_board()
        print('Player 1 wins!')
        sleep(2)
        keep_playing()

    else:
        player2['score'] += 1
        draw_header('game')
        draw_board()
        print('Player 2 wins!')
        sleep(2)
        keep_playing()

def keep_playing():
    global game_on
    global game_count
    global turn
    global game
    answer =''
    while len(answer) == 0:
        answer = input('Play again? (Y)es or (N)o\n>').lower()
        if 'y' in answer:
            game_count += 1
            game = False
            turn = 0
        elif 'n' in answer:
            game = False
            game_on = False
        else:
            print('Invalid response, please enter (Y)es or (N)o')

def play_game(player_turn):

    global turn
    global board

    draw_header('game')
    draw_board('play')
    placed = False
    # takes user input, and run check_space()
    place = ''

    while placed == False:

        if player_turn == 'player1':
            place = input('Player 1, make your move.\n>')
        else:
            place = input('Player 2, make your move.\n>')

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
    turn += 1


def check_turn():
    #binding to parent player_turn
    global player_turn
    # If turn = 0 or turn is even, first person in turn_order plays.  If turn is odd, second person in turn_order plays.
    if turn == 0 or turn % 2 == 0:
        player_turn = turn_order['first']
    else:
        player_turn = turn_order['second']

def main_loop():
    global turn
    global board
    global game

    while game_on == True:
        game = True
        init_board()
        #Initialize player token on first playthrough.  Token is the letter player is using for their game piece.
        if player1['init'] == False & player2['init'] == False:
            init_players()
        draw_header('pre_game')
        input('Press Enter when ready to start!')
        # Game start
        coin_flip()
        while game == True:
            if turn <= 3:
                check_turn()
                play_game(player_turn)
            elif turn >= 4:
                check_turn()
                play_game(player_turn)
                if winner(player_turn):
                    game_over(player_turn)
            elif turn == 9:
                check_turn()
                take_turn(player_turn)
                if winner(player_turn):
                    game_over(player_turn)
                else:
                    game_over('stalemate')

main_loop()
print('Good bye!')
