"""
Author: Christine Wei
Date: 27/02/22
Description: prints asteriks pattern
"""

for row in range(1, 7):
    for column in range(6, row, -1):
        print("*", end=" ")
    print()

print("\n")

for row in range(1, 9):
    for column in range(1, 9):
        print("*", end=" ")
    print()
