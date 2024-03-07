"""
Author: Christine Wei
Date: March 24, 2023,
Description: Converts phrase given by user into pig latin
"""


# main line logic
def main():
    """
    Input: None
    Output: String (piglatin version of user input)
    Description: Displays piglatin version of phrase that the user enters
    """
    # asks user for phrase
    user_string = input("Enter a phrase for me to convert to piglatin: ")
    # turns phrase into piglatin by running it through pig_latin function
    pig_user_string = pig_latin(user_string)
    # displays new piglatin phrase
    print(pig_user_string)


# pig latin translates string into piglatin
def pig_latin(string):
    """
    Input: String (argument expected is all letters)
    Output: String (returns piglatin of input string)
    Description: Converts text to piglatin
    """
    # algorithm for piglatin
    pig_string = string[1:] + string[0] + "ay"
    # returns piglatin
    return pig_string


# run main
main()
