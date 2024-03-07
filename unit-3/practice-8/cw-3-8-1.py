"""
Author: Christine Wei
Date: April 1, 2023,
Description: Find the greatest common denominator (GCD) of 2 numbers
"""


def main():
    """
    Mainline logic,
    Created to test the gcd() function
    Accepts no parameters
    Displays the two numbers and their GCD
    """
    num1 = 81
    num2 = 24

    result = gcd(num1, num2)

    print(f"The two numbers are: {num1}, {num2}. Their GCD is {result}")


def gcd(m, n):
    """
    Function uses recursion to calculate the greatest common denominator of 2 numbers
    It accepts two integers, m and n
    It returns the GCD as an integer
    """

    # base case, if the n is 0, then the greatest common factor is m
    if n == 0:
        return m

    # if n is greater than zero, then the gcf function is run on n and m%n until n is equal to 0
    elif n > 0:
        return gcd(n, m % n)


main()
