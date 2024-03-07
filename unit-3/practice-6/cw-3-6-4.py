"""
Author: Christine Wei
Date: March 30, 2023,
Description: Gets five unique values and displays values
"""


def five_numbers():
    """
    Functions asks user for a number
    If the number they input has already been inputted, it asks again
    If the number they inputted has not been inputted, it is added to the list of numbers
    Continues until the list is five numbers long
    Displays the list
    Takes in no arguments, outputs a list of five items
    """
    num_list = []

    # gets five numbers
    for i in range(5):
        while True:
            # gets number from user
            num = str(input(f"Enter number #{i + 1}: "))

            # if the number is already in the list, it is not added and instead user is asked to re-enter valid input
            if num in num_list:
                continue
            # If the number is not in the list, it is added to the list
            else:
                num_list.append(num)
                break

    # displays the list of five numbers
    print(num_list)


five_numbers()
