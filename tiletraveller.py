# Constants

NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

YES = "y"
NO = "n"

COIN_LOCATIONS = [(1,2), (2,2), (2,3), (3,2)]

import random


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions 

def play_one_move(col, row, valid_directions,coin):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice([NORTH, EAST, SOUTH, WEST]) # tölvan velur random átt
    print("Direction: {}".format(direction)) 

    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        if (col, row) in COIN_LOCATIONS:
            coin = pull_the_lever(coin)
    return victory, col, row, coin


def pull_the_lever(coin):
    anwser = random.choice([YES, NO])  # látum velja random
    print("Pull a lever (y/n): {}".format(anwser)) # biðjum ekki lengur um input, heldur prentum bara
    if anwser == YES:
        coin += 1
        print("You received 1 coin, your total is now {}.". format(coin))
    elif anwser == NO:
        pass
    return coin
    

def play():
    seed_input = int(input("Input seed: ")) # bið notanda um seed fjölda
    random.seed(seed_input) # geri random af seed inputinu

    victory = False
    row = 1
    col = 1
    coin = 0

    counter = 0 # núllstylli counterinn til að geta talið moves

    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, coin = play_one_move(col, row, valid_directions,coin)
        counter += 1 # counterinn hækkar
    print("Victory! Total coins {}. Moves {}.". format(coin,counter))

# The main program starts here    
play_again = YES

while play_again == YES:
    play()
    play_again = input("Play again (y/n): ")



