"""
Author: Christine Wei
Date: 27/02/22
Description:
Program that asks user for number 1-10 \
validates user input \
prints number if number is valid
"""

while True:
    num = int(input("Please enter a number from 1 to 10: "))
    if 1 <= num or num >= 10:
        print(num)
        break
    else:
        print("That number is not between 1 and 10")
        continue
