"""
Author: Christine Wei
Date: 27/02/22
Description: Displays multiplication table
"""

for row in range(1, 11):
    for column in range(1, 11):
        print(row*column, end=" ")
    print()
