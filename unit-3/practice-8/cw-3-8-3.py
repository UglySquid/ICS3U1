"""
Author: Christine Wei
Date: April 1, 2023,
Description: Finds the sum of all number from 1 to the number given as argument
"""


def main():
    """
    Mainline logic,
    Created to test the multiplication() function
    Accepts no parameters
    Displays the number and the sum of the series 1, 2, 3, ... number given
    """
    num1 = 5
    result = add_until_one(num1)

    print(f"The number is: {num1}. The sum of the series: 1, 2, 3, ... {num1} is {result}")


def add_until_one(x):
    """
    Recursive function that accepts an integer argument
    Returns the sum of all the integers from 1 up to the number
    """
    if x == 0:
        return 0
    else:
        return x + add_until_one(x-1)


main()
