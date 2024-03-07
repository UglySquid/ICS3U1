"""
Author: Claudia Gee and Jeremy Liu
Date: 23/04/19
Description: Unit 3 - tictactix assignment
"""

# imports random
import random

def main():
    """
    Description:    This is the main function. It decides who goes first, sets the three ttt boards,
                    and calls all the functions
    Parameters:     none
    Return:         none
    """
    try:
        count = 0
        # opens the hall_of_fame.txt file
        fame_r = open('Hall_of_fame.txt', 'r')

        # displays the hall of fame and each name with a rank in front of it
        print(" -------- + -------- HALL OF FAME  -------- + -------- " + "\n")
        for line in fame_r:
            count += 1
            print(str(count) + "." + line)

        fame_r.close()

    except IOError:
        # outputs computer message
        print("\n" + "No Human Has Ever Beat Me... mwah-ha-ha-ha!" + "\n")

    # initializes variables
    users_turn = True
    free_cells = 26

    # empty list
    ttt_board1 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    ttt_board2 = [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]]
    ttt_board3 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # greets the user
    print("Welcome to tictactix!")
    display_all(ttt_board1, ttt_board2, ttt_board3)

    # chooses who goes first
    first_play = input("Would you like to go first? Type Y or N: ")

    # if the user enters a no-value input, itll asked the user again
    while (first_play != "Y" and first_play != "y" and first_play != "N" and first_play != "n"):
        print("invalid choice, please repick!")
        first_play = input("Would you like to go first? Type Y or N: ")

    # after the user answers accordingly...
    if first_play == "Y" or first_play == "y":
        # allows the user to go first
        user_move(ttt_board1, ttt_board2, ttt_board3)
        users_turn = False

    elif first_play == "n" or first_play == "N":
        # calls the computer to go first
        computer_move(ttt_board1, ttt_board2, ttt_board3)
        users_turn = True

    # while nobody wins yet, we continue the game
    while not winner_board(ttt_board1, ttt_board2, ttt_board3) and free_cells > 0:
        if users_turn:
            #allows user to go
            print("** USER TURN **")
            user_move(ttt_board1, ttt_board2, ttt_board3)
            users_turn = not users_turn

        else:
            #allows computer to go
            print("** COMPUTER MOVE **")
            computer_move(ttt_board1, ttt_board2, ttt_board3)
            users_turn = not users_turn

        free_cells -= 1
        # each time this while loop runs, a free cell will be substracted from 26
        if winner_board(ttt_board1, ttt_board2, ttt_board3) == "X":
            print("Y O U   W O N !")

            # asks for the winner's name and if it is not on the hall of fame the computer will add it to the file
            win_name = input("Now tell me your name so I can add you to the Hall of Fame: ")
            fame_r = open("Hall_of_fame.txt", "r")
            fame_a = open("Hall_of_fame.txt", "a")

            while win_name in fame_r:
                print("Type in a different name!")
                win_name = input("Now tell another name so I can add you to the Hall of Fame: ")

            fame_a.write(win_name + "\n")
            print("I've added your name to the hall of fame, thanks for playing!")
            fame_a.close()
            fame_r.close()

        #computer wins
        elif winner_board(ttt_board1, ttt_board2, ttt_board3) == "O":
            print("I   W O N !")

        # displays tie
        elif free_cells == 0:
            print("S T A L E M A T E !")


def display_all(ttt_board1, ttt_board2, ttt_board3):
    """
    Description:    Allows for one function to call all three boards for efficiency
    Parameter:      ttt_board1, ttt_board2, ttt_board3
    Returns:        None
    """
    #displays the three boards
    display_board1(ttt_board1)
    display_board2(ttt_board2)
    display_board3(ttt_board3)


def display_board1(ttt_board1):
    """
    Description:    This function displays the board of the three tic-tac-toe boards,
                    with appropriate comments and labels differentiating the boards
    Parameters:     none
    return:         none
    """
    # board no.1
    print("                0      1      2")
    print("             ----- + ----- + -----")
    print("0:        /   " + ttt_board1[0][0] + "   /   " + ttt_board1[0][1] + "   /   " + ttt_board1[0][2] + "   /   ")
    print("          - - - + - - - + - - -")
    print("1:     /   " + ttt_board1[1][0] + "   /   " + ttt_board1[1][1] + "   /   " + ttt_board1[1][2] + "   /   ")
    print("        - - - + - - - + - - -")
    print("2:  /   " + ttt_board1[2][0] + "   /   " + ttt_board1[2][1] + "   /   " + ttt_board1[2][2] + "   /   ")
    print("     - - - + - - - + - - -")
    print()


def display_board2(ttt_board2):
    """
    Description:    This function displays the board of the three tic-tac-toe boards,
                    with appropriate comments and labels differentiating the boards
    Parameters:     none
    return:         none
       """
    # board no.2
    print("                       ")
    print("             - - - + - - - + - - -")
    print("3:        /   " + ttt_board2[0][0] + "   /   " + ttt_board2[0][1] + "   /   " + ttt_board2[0][2] + "   /   ")
    print("          - - - + - - - + - - -")
    print("4:     /   " + ttt_board2[1][0] + "   /   " + ttt_board2[1][1] + "   /   " + ttt_board2[1][2] + "   /   ")
    print("        - - - + - - - + - - -")
    print("5:  /   " + ttt_board2[2][0] + "   /   " + ttt_board2[2][1] + "   /   " + ttt_board2[2][2] + "   /   ")
    print("     - - - + - - - + - - -")
    print()


def display_board3(ttt_board3):
    """
    Description:    This function displays the board of the three tic-tac-toe boards,
                    with appropriate comments and labels differentiating the boards
    Parameters:     none
    return:         none
       """
    # board no.3
    print("                                     ")
    print("             - - - + - - - + - - -")
    print("6:        /   " + ttt_board3[0][0] + "   /   " + ttt_board3[0][1] + "   /   " + ttt_board3[0][2] + "   /   ")
    print("          - - - + - - - + - - -")
    print("7:     /   " + ttt_board3[1][0] + "   /   " + ttt_board3[1][1] + "   /   " + ttt_board3[1][2] + "   /   ")
    print("        - - - + - - - + - - -")
    print("8:  /   " + ttt_board3[2][0] + "   /   " + ttt_board3[2][1] + "   /   " + ttt_board3[2][2] + "   /   ")
    print("     - - - + - - - + - - -")
    print()
    print("+ ------------------------------------------------------------------------- +")


def user_move(ttt_board1, ttt_board2, ttt_board3):
    """
    Description:    This function allows the user to input their turn
    Parameters:     ttt_board1, ttt_board2, ttt_board3, the three boards
    Return:         none
    """
    # initializes the initial valid move as false, to continue the game
    valid_move = False
    while not valid_move:

    # from the users answer itll run through each if statement and proceed to ask what column and row to play
        layer_num = int(input("What layer would you like to play(1 - 3): "))

        if layer_num == 1:
            column = int(input("What column would you like to play (0 - 2): "))
            row = int(input("What row would you like to play (0 - 2): "))

            if (0 <= int(row) <= 2) and (0 <= int(column) <= 2) and (ttt_board1[int(row)][int(column)] == " "):
                ttt_board1[int(row)][int(column)] = 'X'
                display_all(ttt_board1, ttt_board2, ttt_board3)
                valid_move = True

            else:
                # makes the user try again if there is an invalid square
                print("Sorry, invalid square. Please try again!\n")

        elif layer_num == 2:
            column = int(input("What column would you like to play (0 - 2): "))
            row = int(input("What row would you like to play (3 - 5): ")) - 3

            if (0 <= int(row) <= 2) and (0 <= int(column) <= 2) and (ttt_board2[int(row)][int(column)] == " "):
                ttt_board2[int(row)][int(column)] = 'X'
                display_all(ttt_board1, ttt_board2, ttt_board3)
                valid_move = True

            else:
                # makes the user try again if there is an invalid square
                print("Sorry, invalid square. Please try again!\n")

        elif layer_num == 3:
            column = int(input("What column would you like to play (0 - 2): "))
            row = int(input("What row would you like to play (6 - 8): ")) - 6

            if (0 <= int(row) <= 2) and (0 <= int(column) <= 2) and (ttt_board3[int(row)][int(column)] == " "):
                ttt_board3[int(row)][int(column)] = 'X'
                display_all(ttt_board1, ttt_board2, ttt_board3)
                valid_move = True

            else:
                # makes the user try again if there is an invalid square
                print("Sorry, invalid square. Please try again!\n")

        elif layer_num != 1 or layer_num != 2 or layer_num != 3:
            print("No such layer. Try again!")
            valid_move = False


def computer_move(ttt_board1, ttt_board2, ttt_board3):
    """
    Description:    This function allows the user to input their turn
    Parameters:     ttt_board1, ttt_board2, ttt_board3, the three boards
    Return:         none
    """

    valid_move = False
    while not valid_move:

        # has the computer choose a random number between the ranges
        layer = random.randint(1, 3) - 1
        row = int(random.randint(0, 2))
        column = int(random.randint(0, 2))
        boards = [ttt_board1, ttt_board2, ttt_board3]

        # creates a variable to store each board individually
        board = boards[layer]

        # checks if the computer move is valid, and then plays the move for it
        if (0 <= (row) <= 2) and (0 <= (column) <= 2) and (board[row][column] == " "):
            board[row][column] = 'O'
            display_all(ttt_board1, ttt_board2, ttt_board3)
            valid_move = True
        else:
            valid_move = False


def winner_board(ttt_board1, ttt_board2, ttt_board3):
    """
    Description:    This function retrieves the different board and stack cases to get passed into main
    Parameter:      ttt_board1, ttt_board2, ttt_board3
    Return:         "O", "X", the space chosen after someone wins
    """

    ttt_boards = [ttt_board1, ttt_board2, ttt_board3]

    # returns O and X if the boards win as O or X, respectively

    # Finds wins in the for every board
    for board in ttt_boards:
        if board_for_winner(board) != "":
            return board_for_winner(board)

    # Finds stacked wins
    return winner_stack(ttt_board1, ttt_board2, ttt_board3)


def board_for_winner(board):
    """
    Description: This function checks for any three in the rows, this function only checks the wins for each layer
    Parameters:
    Returns: ttt_board1, ttt_board2, ttt_board3
    :param board:
    """

    # Check rows for winner
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != " "):
            return board[row][0]

    # Check columns for winner
    for column in range(3):
        if (board[0][column] == board[1][column] == board[2][column]) and (board[0][column] != " "):
            return board[0][column]

    # Check diagonal (top-left to bottom-right) for winner
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != " "):
        return board[0][0]

    # Check diagonal (bottom-left to top-right) for winner
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != " "):
        return board[0][2]

    # No winner: return the empty string
    return ""


def winner_stack(ttt_board1, ttt_board2, ttt_board3):
    """
    Description:    This function focuses on checking if there are any stacked wins
    Parameter:      ttt_board1, ttt_board2, ttt_board3
    Return:         None
    """

    # checks each column stack for wins
    for row in range(3):
        for column in range(3):
            if ttt_board1[row][column] == ttt_board2[row][column] == ttt_board3[row][column] and ttt_board1[row][column] != " ":
                return ttt_board1[row][column]

    # checks each column diagonal for wins
    for column in range(0, 3, 2):
        if ttt_board1[0][column] == ttt_board2[1][column] == ttt_board3[2][column] and ttt_board1[0][column] != " ":
            return ttt_board1[0][column]
        elif ttt_board1[2][column] == ttt_board2[1][column] == ttt_board3[0][column] and ttt_board1[2][column] != " ":
            return ttt_board1[2][column]

    # checks each diagonal for wins
    for row in range(0, 3, 2):
        if ttt_board1[row][0] == ttt_board2[row][1] == ttt_board3[row][2] and ttt_board1[row][0] != " ":
            return ttt_board1[row][0]
        elif ttt_board1[row][2] == ttt_board2[row][1] == ttt_board3[row][0] and ttt_board1[row][2] != " ":
            return ttt_board1[row][2]

    return ""

# mainline logic
main()