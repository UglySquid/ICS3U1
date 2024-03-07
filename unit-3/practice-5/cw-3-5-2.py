"""
Author: Christine Wei
Date: March 28, 2023,
Description: Reverses list
"""


def main():
    """
    Main function used to test list_reverse function
    Accepts no arguments
    Asks user for input
    Displays the user's list with all items reversed
    """

    # test list used to show that this the list_reverse() function works
    test_list = [1, 2, 3, 4, 5, 6, 7, "Hi"]
    reversed_list = list_reverse(test_list)
    print(f"The reversed list for:{test_list} is {reversed_list} ")


def list_reverse(num_list):
    """
    Reverses original list
    Accepts one array as argument
    Returns new array with the input array's elements reversed
    """
    # creates new list with the old list's items reversed
    new_list = num_list[::-1]
    return new_list


main()
