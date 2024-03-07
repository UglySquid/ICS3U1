"""
Author: Christine Wei
Date: April 11, 2023,
Description: 3D Tic Tac Toe Game
"""

import random


def main():
    """Our Main Game Loop:"""

    free_cells = 26

    # The Tic Tac Tix board
    ttt_board = [[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "],
                 [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]]

    # ASks user if they want to have the first turn. If so, they start
    users_turn = first_turn()

    # Asks user what level they wish to play
    level = pick_level()

    # Loops user and computer turns until someone wins or there are no more free cells
    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            # Lets user move
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            if level == 0:
                # Lets computer make smart move
                make_computer_move(ttt_board)
                users_turn = not users_turn
            else:
                # Lets computer make random move
                level_1(ttt_board)
                users_turn = not users_turn
        free_cells -= 1

    display_board(ttt_board)

    # When human player has won
    if winner(ttt_board) == "X":
        print("Y O U   W O N !")
        # Adds human name to hall of fame
        try:
            with open("HallOfFame.txt", "r") as fr:
                for line in fr:
                    print(line.strip())
        except FileNotFoundError:
            print("“No Human Has Ever Beat Me...mwah-ha-ha-ha!")

        with open("HallOfFame.txt", "a") as fa:
            fa.write(input("What is your name? ")+"\n")

    # When computer has won
    elif winner(ttt_board) == 'O':
        print("I   W O N !")

    # When no one has won but there are no more free cells
    else:
        print("S T A L E M A T E !")

    print("\n*** GAME OVER ***\n")


def pick_level():
    """
    Description: Asks user to pick a level
    Input (Parameters): Accepts nothing as argument
    Output: returns the level human user has chosen
    """

    while True:
        try:
            level = int(input("What level would you like to play? Respond with 0 or 1: "))

            # If the level is not one of the available levels
            if level == 0 or level == 1:
                return level
            else:
                print("That is not a valid level")
        # If the level inputted is not a number
        except ValueError:
            print("That is not a valid input")
            continue


def first_turn():
    """
    Description: Asks user if they would like to go first
    Input (Parameters): Accepts nothing as argument
    Output: returns the boolean True if they want to go first, False if they don't want to go first
    """

    while True:
        # Asks user if they want to go first
        first = input("Would you like to go first? Respond with y or n: ")

        # If user wants to go first, returns true
        if first == "y" or first == "Y":
            return True
        # If user does not want to go first, returns false
        elif first == "n" or first == "N":
            return False
        # If user input is not y, Y, n, or N, user is asked to re-input
        else:
            print("That is not a valid input")
            continue


def display_board(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will print the Tic-Tac-Toe board grid (using ASCII characters)
    and show the positions of any X's and O's.  It also displays
    the column and row numbers on top and beside the board to help
    the user figure out the coordinates of their next move.
    This function does not return anything."""

    # Displays layer 1
    print("              1     2     3")
    print("          ------+-----+-----")
    print(f"      1: /  {board[0][0][0]}  /  {board[0][0][1]}  /  {board[0][0][2]}  /|")
    print("        +-----+-----+-----  |")
    print(f"    2: /  {board[0][1][0]}  /  {board[0][1][1]}  /  {board[0][1][2]}  /  |  layer 1")
    print("      +-----+-----+-----    |")
    print(f"  3: / {board[0][2][0]}  /  {board[0][2][1]}  /  {board[0][2][2]}  /     |")
    print("    +-----+-----+-----      |")
    print("    |                       |")

    # Displays layer 2
    print("    |     ------+-----+-----|")
    print(f"    | 1: /  {board[1][0][0]}  /  {board[1][0][1]}  /  {board[1][0][2]}  /|")
    print("    |   +-----+-----+-----  |")
    print(f"    2: /  {board[1][1][0]}  /  {board[1][1][1]}  /  {board[1][1][2]}  /  |  layer 2")
    print("    | +-----+-----+-----    |")
    print(f"  3:|/  {board[1][2][0]}  /  {board[1][2][1]}  /  {board[1][2][2]}  /    |")
    print("    |+-----+-----+-----     |")
    print("    |                       |")

    # Displays layer 3
    print("    |     ------+-----+-----")
    print(f"    | 1: /  {board[2][0][0]}  /  {board[2][0][1]}  /  {board[2][0][2]}  /")
    print("    |   +-----+-----+-----")
    print(f"    2: /  {board[2][1][0]}  /  {board[2][1][1]}  /  {board[2][1][2]}  /  layer 3")
    print("    | +-----+-----+-----")
    print(f"  3:|/  {board[2][2][0]}  /  {board[2][2][1]}  /  {board[2][2][2]}  /")
    print("    +-----+-----+-----")

    print("\n+======================================================================+\n")


def make_user_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
        It will ask the user for a row and column.  If the row and
        column are each within the range of 0 and 2, and that square
        is not already occupied, then it will place an 'X' in that square."""

    while True:
        try:
            # Asks user what layer, row, and column they want to place their "X"
            layer = int(input("What layer would you like to move to (1-3): ")) - 1
            row = int(input("What row would you like to move to (1-3): ")) - 1
            col = int(input("What col would you like to move to (1-3): ")) - 1

            # If the input is a valid tile, and if the tile is empty, "X" is placed
            if (0 <= layer <= 2) and (0 <= row <= 2) and (0 <= col <= 2) and (board[layer][row][col] == " "):
                board[layer][row][col] = "X"
                break
            # If input is an invalid number, or if tile is filled, user is asked to choose a different tile
            else:
                print("Sorry, invalid square. Please try again!\n")
                continue
        # If input is not a number, user is asked to choose a different tile
        except ValueError:
            print("Sorry, invalid square. Please try again!\n")
            continue


def make_computer_move(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will randomly pick row and column values between 0 and 2.
    If that square is not already occupied it will place an 'O'
    in that square.  Otherwise, another random row and column
    will be generated."""

    while True:
        # Picks random row value and random column value
        layer, row, column = random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)

        # Changes the value at random position
        if board[layer][row][column] == " ":
            board[layer][row][column] = "O"
            break
        else:
            continue


def winner(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
        If there is no winner, the function will return the empty string "".
        If the user has won, it will return 'X', and if the computer has
        won it will return 'O'."""

    # Finds wins in the 2D scope for every layer
    for layer in range(3):
        if winner_2d(board[layer]) != "":
            return winner_2d(board[layer])

    # Finds wins in the 3D scope
    return winner_3d(board)


def winner_2d(layer):
    """
    Description: Checks all possible combinations in the 2D scope for wins and returns whoever has won.
                 If no one has won, an empty string is returned.
    Input (Parameters): Accepts layer as parameter
    Output: Returns "X" if human has won, "O" if computer has won, and "" (empty string) if no one has won
    """

    # Check rows for winner
    for row in range(3):
        if (layer[row][0] == layer[row][1] == layer[row][2]) and (layer[row][0] != " "):
            return layer[row][0]

    # Check columns for winner
    for column in range(3):
        if (layer[0][column] == layer[1][column] == layer[2][column]) and (layer[0][column] != " "):
            return layer[0][column]

    # Check diagonal (top-left to bottom-right) for winner
    if (layer[0][0] == layer[1][1] == layer[2][2]) and (layer[0][0] != " "):
        return layer[0][0]

    # Check diagonal (bottom-left to top-right) for winner
    if (layer[0][2] == layer[1][1] == layer[2][0]) and (layer[0][2] != " "):
        return layer[0][2]

    # No winner: return the empty string
    return ""


def winner_3d(board):
    """
    Description: Checks all possible combinations in the 3D scope for wins and returns whoever has won.
                 If no one has won, an empty string is returned.
    Input (Parameters): Accepts layer as parameter
    Output: Returns "X" if human has won, "O" if computer has won, and "" (empty string) if no one has won
    """

    # Check vertical interlayer wins
    for column in range(3):
        for row in range(3):
            if (board[0][row][column] == board[1][row][column] == board[2][row][column]) and (board[0][row][column] != " "):
                return board[0][row][column]

    # Check diagonal interlayer wins (top-left to bottom-right)
    for row in range(0, 3, 2):
        if (board[0][row][0] == board[1][row][1] == board[2][row][2]) and (board[0][row][0] != " "):
            return board[0][row][0]

    for col in range(0, 3, 2):
        if (board[0][0][col] == board[1][1][col] == board[2][2][col]) and (board[0][0][col] != " "):
            return board[0][0][col]

    # Check diagonal interlayer wins (bottom-left to top-right)
    for row in range(0, 3, 2):
        if (board[0][row][2] == board[1][row][1] == board[2][row][0]) and (board[0][row][2] != " "):
            return board[0][row][2]

    for col in range(0, 3, 2):
        if (board[0][2][col] == board[1][1][col] == board[2][0][col]) and (board[0][2][col] != " "):
            return board[0][2][col]

    # No winner: return the empty string
    return ""


def level_1(board):
    """
    Computer foresees the obvious path to win for itself
    and to prevent the obvious potential winner from their opponent from
    playing a bet to prevent it.
    """

    temp_board = board

    # Finds when computer is about to win. This is played if user has no way of winning
    for layer in range(3):
        for row in range(3):
            for tile in range(3):
                # Changes blank tile to "O"
                if board[layer][row][tile] == " ":
                    board[layer][row][tile] = "O"
                    # If this change causes computer to win
                    if winner(board) == "O":
                        # "O" is placed to make computer win
                        board[layer][row][tile] = "O"
                        return
                    # If "O" placed does not result in win, then it is replaced by blank " "
                    else:
                        board[layer][row][tile] = " "

    # Prevents the player from winning, this is placed after is computer does not find a winning move
    for layer in range(3):
        for row in range(3):
            for tile in range(3):
                # Changes blank tile to "X"
                if board[layer][row][tile] == " ":
                    board[layer][row][tile] = "X"
                    # If this change causes player to win
                    if winner(board) == "X":
                        # "O" is placed to prevent player form winning
                        board[layer][row][tile] = "O"
                        return
                    # If "X" placed does not result in win, then it is replaced by blank " "
                    else:
                        board[layer][row][tile] = " "

    if temp_board == board:
        while True:
            # If there are no winning moves, computer picks random row value and random column value
            if temp_board == board:
                layer, row, column = random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)

                # Changes the value at random position
                if board[layer][row][column] == " ":
                    board[layer][row][column] = "O"
                    break
                else:
                    continue


# start game
main()
