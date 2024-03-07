"""
Author: Christine Wei
Date: March 28, 2023,
Description: Doubles every item in the list
"""


def main():
    """
    Main line logic
    Does not accept any arguments
    Displays a doubled list
    """

    test_list = [1, 2, 3.0, 4, 5.8, 6, 7]
    doubled_list = double_it(test_list)

    print(f"The doubled list for:{test_list} is {doubled_list} ")


def double_it(num_list):
    """
    Doubles the values of numbers in the list
    Expects list argument
    Returns list with all values in input list doubled
    """

    # Iterates through all the indexes in the list
    for index in range(0, len(num_list)-1):
        # For every index, multiply the number at the index by two
        num_list[index] *= 2

    return num_list


main()
