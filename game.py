row1 = ["#"," "," "," "," "," "," "," "," "," "]

def display_board(row1):

    print(row1[1:4])
    print(row1[4:7])
    print(row1[7:])

def marker_selection():

    player1marker = " "

    print("Hello Player 1!")
    while player1marker not in ["X","O"]:
        player1marker = input("Please select X or O: ").upper()

    if player1marker == "X":
        return ("X","O")
    else:
        return ("O","X")

def playerinput(row1,marker1):

    player1input = "Wrong Choice"
    acceptableinputs = ["9","1","2","3","4","5","6","7","8"]

    while player1input.isdigit() == False or player1input not in acceptableinputs:
        player1input = input("Please select a position number from 1-9: ")

    return int(player1input)

def space_check(row1,position):

    return row1[position] == " "

def full_board_check(row1):

    for i in range(1,10):

        if space_check(row1,i):
            return False

    return True

def position_choice(row1):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(row1,position):

        position = int(input("Please enter a position from 1 - 9 : "))

    return position

def replay():

    choice = input("Do you want to play again ? Enter Yes or No: ")

    return choice == "Yes"

import random


def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

def place_marker(row1,position,marker):

    row1[position] = marker

def win_check(row1,mark):

    return ((row1[1] == player1 and row1[2] == player1 and row1[3] == player1)or
    (row1[4] == player1 and row1[5] == player1 and row1[6] == player1)or
    (row1[7] == player1 and row1[8] == player1 and row1[9] == player1)or
    (row1[1] == player1 and row1[4] == player1 and row1[7] == player1)or
    (row1[2] == player1 and row1[5] == player1 and row1[8] == player1)or
    (row1[3] == player1 and row1[6] == player1 and row1[9] == player1)or
    (row1[7] == player1 and row1[5] == player1 and row1[3] == player1)or
    (row1[1] == player1 and row1[5] == player1 and row1[9] == player1))

print("Welcome")

while True:




    player1,player2 = marker_selection()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n ?")
    if play_game == "y":
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == "Player 1":

            display_board(row1)

            position = position_choice(row1)

            place_marker(row1,position,player1)

            if win_check(row1,player1):
                display_board(row1)
                print("Player 1 Won !!!")
                game_on = False

            else:
                if full_board_check(row1):
                    display_board(row1)
                    print("Tie Game")
                    game_on = False

                else:
                    turn = "Player 2"

        else:
            display_board(row1)

            position = position_choice(row1)

            place_marker(row1,position,player2)

            if win_check(row1,player2):
                display_board(row1)
                print("Player 2 Won !!!")
                game_on = False

            else:
                if full_board_check(row1):
                    display_board(row1)
                    print("Tie Game")
                    game_on = False

                else:
                    turn = "Player 1"



    if not replay():
        break

    
