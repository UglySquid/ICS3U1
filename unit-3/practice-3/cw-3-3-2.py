"""
Author: Christine Wei
Date: March 24, 2023,
Description: Converts phrase given by user into pig latin
"""


# functions that detects white space
def contains_whitespace(text):
    """
    Input: String (text)
    Output: Boolean (True if there is white space, false if there is no whitespace)
    Description: Checks if there is whitespace in text
    """
    # if there is white space
    if ('' or '\t' or '\n') in text:
        # returns boolean True
        return True
    # if there isn't whitespace
    else:
        # return boolean false
        return False
