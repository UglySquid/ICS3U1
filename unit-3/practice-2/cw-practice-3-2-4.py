"""
Author: Christine Wei
Date: March 21, 2023,
Description: Asks user for file, displays contents of file
"""

# asks user what file they want to display
user_file = input("Type in the name fo the file you want to display: ")

# sets first line as zero
file_line = 0

# try except block that makes sure the user's file exists
try:
    # opens file user wants to display
    file_name = open(user_file, 'r')
    # for every line in file, it displays the line number and the contents of the line
    for line in file_name:
        file_line += 1
        print(file_line, ": ", line.strip())
except IOError:
    print("This file does not exist or could not be found. Please try again.")


