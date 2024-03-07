"""
Author: Christine Wei
Date: March 27, 2023,
Description: Translates letters in phone numbers into numbers
"""


def tele_num(telephone_num):
    """
    Accepts telephone number as string input
    Returns telephone number as integer
    """
    telephone_num = telephone_num.strip("-")
    telephone_num = telephone_num.upper()

    for character in telephone_num:
        if not character.isalpha():
            continue
        else:
            if character in "ABC":
                character_num = 2
            elif character in "DEF":
                character_num = 3
            elif character in "GHI":
                character_num = 4
            elif character in "JKL":
                character_num = 5
            elif character in "MNO":
                character_num = 6
            elif character in "PQRS":
                character_num = 7
            elif character in "TUV":
                character_num = 8
            elif character in "WXYZ":
                character_num = 9

            telephone_num = telephone_num.replace(character, str(character_num))

    print(telephone_num)


tele_num(input("Give telephone number: "))
