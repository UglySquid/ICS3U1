"""
Author: Christine Wei
Date: April 1, 2023,
Description: Find the number to an exponent
"""


def main():
    """
    Mainline logic,
    Created to test the exponent() function
    Accepts no parameters
    Displays the two numbers and their product
    """
    num = 4
    num_exponent = 3

    result = exponent(num_exponent, num)

    print(f"The number is: {num} and the exponent is: {num_exponent}. The power is {result}")


def exponent(x, y):
    """
    Function uses recursion to calculate the power of a number
    It accepts two integers, x and y, representing the exponent and the number
    It returns the power
    """
    if x == 0:
        return 1
    else:
        return y * exponent(x-1, y)


main()
