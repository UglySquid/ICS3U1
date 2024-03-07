"""
Author: Christine Wei
Date: March 6, 2023,
Description: Calculates and displays
the distance between the two lines
and the slope of the line
"""

# import the math module
import math


def main():
    """
    Mainline logic
    Asks user for x and y coordinates of two points
    calculates the distance and slope of the line of two points
    displays distance and slope
    """

    # asks for the coordinates of the two points
    x1, y1 = int(input("Input the x-coordinate #1: ")), int(input("Input the y-coordinate #1: "))
    x2, y2 = int(input("Input the x-coordinate #2: ")), int(input("Input the y-coordinate #2: "))

    # calculates the distance and the slope
    distance, slope = calculate(x1, y1, x2, y2)

    # displays the distance and the slope
    print("The distance between the two points is ", distance)
    print("The slope of the lien is ", slope)


def calculate(x1, y1, x2, y2):
    """
    Calculates the slope and distance between two points
    Takes in the x and y values of 2 coordinates as integers
    Returns the distance and then the slope
    """

    # calculates the distance and the slope
    distance = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
    slope = (y2 - y1)/(x2 - x1)

    # return the distance and slope
    return distance, slope


main()
