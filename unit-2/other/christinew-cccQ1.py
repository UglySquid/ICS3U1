
"""
Author: Christine Wei
Date: 23/02/22
Description: Determines Barley's happiness score
"""

# Gets string input from user to show how many of each type of treat was given to Barley
def main():
    """
    Takes in user input from keyboard, \
    outputs string phrase that descrives Barley's happiness
    """
    num_s = int(input())
    num_m = int(input())
    num_l = int(input())
    happy_score = calculate_happy_score(num_s, num_m, num_l)
    display_happiness(happy_score)

# Calculates Barley's happy score
def calculate_happy_score(small, medium, large):
    """
    Takes in 3 integers that shows how many of each treat were given, \
    calculates happiness score, \
    returns score calculated score
    """
    happy_score = 1*small + 2*medium + 2*large
    return happy_score

# Displays happyiness score
def display_happiness(happy_score):
    """
    Takes in happiness score, \
    Prints string statement based on how high score is
    """
    if happy_score >= 10:
        print("happy")
    else:
        print("sad")

main()