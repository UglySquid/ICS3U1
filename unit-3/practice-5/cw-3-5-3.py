"""
Author: Christine Wei
Date: March 28, 2023,
Description: Finds the sum of all the number in a list
"""


def main():
    """
    Main function used to test total() function
    Accepts no arguments
    Displays the results from using test list as argument in total() function
    """

    # test list used to show that the total() function works
    test_list = [1, 2, 3, 4, 5, 6, "Hi", 7]
    test_sum = total(test_list)
    print(f"The sum of: {test_list} is {test_sum}")


def total(num_list):
    """
    Total function find the sum of all numeric items in list
    Accepts list as argument
    If there are no numbers, function returns zero
    If there are, the sum of all numbers is found and returned as an integer
    """

    num_sum = 0

    for num in num_list:
        # Checks if the list item is a number
        if str(num).isnumeric():
            # If list item is a number, it's value is added to the sum
            num_sum += num
        else:
            # If list item is not a number, it is skipped
            continue

    return num_sum


main()
