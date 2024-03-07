"""
Author: Christine Wei
Date: March 9, 2023,
Description: Python module that contains functions get_digit, is_ISBN10, and is_ISBN13
"""


def get_digit(number, position):
    """
    Accepts two integer arguments (number to get digit from, and position of digit)
    Returns integer digit that is found in the position specified
    """

    # When the position is greater than 0.
    if position > 0:
        # When the position is past the left-most digit, it is 0.
        if (number % 11 == 0 and position > 10) or (number % 13 == 0 and position > 10):
            digit = 0
        # When the position is not past the left-most digit, it returns the digit it finds at that position.
        else:
            digit = (number % (10 ** position)) // 10 ** (position - 1)
    # When the position is 0, above formula does not work, and it must go through this else statement.
    else:
        # Calculates the check digit
        if number % 11 == 0:
            digit = number % 10//10
        else:
            digit = number % 10//12

    return digit


def is_ISBN10(number):
    """
    Accepts number argument as integer. This integer should be a 10 digit ISBN code
    Checks validity of ISBN code
    Returns Boolean True if is it valid and False if it is invalid
    """

    digit_validity = 0

    # Algorithm for validating ISBN code.
    for position in range(1, 10):
        # Excluding the check digit, multiplies each digit by the position it is found, take the sum of their products.
        digit_validity += position*get_digit(number, 11-position)

    # Divide the sum found above and take the remainder.
    digit_validity %= 11

    # If the final number is equal to the check digit, then in is valid. If not, it is invalid.
    if number % 10 == digit_validity:
        return True
    else:
        return False


def is_UPC12(number):
    """
    Accepts number argument as integer. This integer should be a 12 digit UPC code
    Checks validity of UPC code
    Returns Boolean True if is it valid and False if it is invalid
    """
    digit_validity = 0
    even_sum = 0

    # Takes the sum of all digits in odd positions.
    for position in range(1, 13, 2):
        digit_validity += get_digit(number, 14-position)

    # Multiplies the sum of digits in odd positions by 3.
    digit_validity *= 3

    # Takes the sum of all digits in even positions.
    for position in range(2, 11, 2):
        even_sum += get_digit(number, 12-position)

    # Add the product of 3 and the sum of odd position digits with the sum of even position digits
    digit_validity += even_sum

    # Divides above sum by 10 and takes the remainder
    digit_validity = digit_validity % 10

    # If the final number is equal to the check digit, then in is valid. If not, it is invalid.
    if number % 10 == digit_validity:
        return True
    else:
        return False
