"""
Author: Christine Wei
Date: March 28, 2023,
Description:
"""


def remove_negs(num_list):
    """
    Remove the negative numbers from the list num_list.
    Accepts list input
    outputs list without all negative numbers
    """

    # List so that I can use len() and not create an index error when each item is removed
    new_list = []
    for item in range(0, 8):
        # if the number is not negative it will add it to the new list
        if num_list[item] < 0:
            continue
        else:
            new_list.append(num_list[item])

    return new_list

# to test the function
print(remove_negs([1, 2, 3, -3, 6, -1, -3, 1]))
