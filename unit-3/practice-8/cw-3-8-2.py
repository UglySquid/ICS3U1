"""
Author: Christine Wei
Date: April 1, 2023,
Description: Find the product of 2 numbers
"""


def main():
    """
    Mainline logic,
    Created to test the multiplication() function
    Accepts no parameters
    Displays the two numbers and their product
    """
    num1 = 4
    num2 = 3

    result = multiplication(num1, num2)

    print(f"The two numbers are: {num1}, {num2}. Their product is {result}")


def multiplication(x, y):
    """
    Function uses recursion to calculate the product of 2 numbers
    It accepts two integers, x and y
    It returns the product as an integer
    """
    if x == 0:
        return 0
    else:
        return y + multiplication(x-1, y)


main()
