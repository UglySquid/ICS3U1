"""
Author: Christine Wei
Date: March 24, 2023,
Description: Checks how many words there are in a phrase
"""


# mainline logic
def main():
    # user input
    user_text = input("Word count: ")
    # number of words in user input
    num_words = word_count(user_text)
    # displays word count
    print(f"There are {num_words} words.")


# word count function counts the number of words in a string
def word_count(text):
    """
    Input: Accepts string (text)
    Output: Returns integer (number of words in text)
    Description: Counts how many words there are in the text
    """

    # initializes the number of words as 1 (0 spaces)
    num_words = 1
    for character in text:
        # everytime space occurs, there is one more word
        if character == " " or character == "\t":
            num_words += 1
        else:
            continue

    # returns the number of words
    return num_words
