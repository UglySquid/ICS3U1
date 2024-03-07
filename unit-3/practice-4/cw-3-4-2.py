"""
Author: Christine Wei
Date: March 27, 2023,
Description: Accepts string and returns integer for number of vowels in string
"""


def main():
    """
    Accepts no arguments
    Displays number of vowels
    """
    vowels = count_vowels("The Quick Brown Fox Jumped Over the Lazy Dog")
    print(vowels)


def count_vowels(string):
    """
    Accepts string input
    Ouputs integer that represents the number of vowels in string input
    """
    num_vowels = 0
    vowels = "aoeiu"
    string = string.lower()
    print(len(string))
    for x in string:
        if x in vowels:
            num_vowels += 1
        else:
            continue

    return num_vowels


main()
