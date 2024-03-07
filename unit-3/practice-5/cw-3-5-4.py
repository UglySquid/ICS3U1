"""
Author: Christine Wei
Date: March 28, 2023,
Description: Function that replaces each value in a list with twice the preceding
value
"""


def main():
    """
    Main function used to test double_preceding() function
    Accepts no arguments
    Displays the results from using test list as argument in double_preceding() function
    """

    # test list used to show that the double_preceding() function works
    test_list = [1, 3, 7, 11]
    pre_double = double_preceding(test_list)
    print(f"The double_preceding of: {[1, 3, 7, 11]} is {pre_double}")


def double_preceding(values):
    temp = [0]
    # For every index in values except for 0
    for i in range(0, len(values)-1):
        # Change the value at that index to double the value at the preceding index. Add changed value to new list
        x = values[i]*2
        temp.append(x)

    return temp


main()
