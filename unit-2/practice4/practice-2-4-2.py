"""
Author: Christine Wei
Date: 27/02/22
Description: displays the largest and smallest of the numbers entered.
"""
num = int(input("Please enter a number (enter negative number to end): "))
smallest_num = num
largest_num = num

while num > 0:
    num = int(input("Please enter a number (enter negative number to end): "))

    if smallest_num > num > 0:
        smallest_num = num
    if num > largest_num:
        largest_num = num
    else:
        continue

print(f"The smallest number is: {smallest_num} \nThe largest number is {largest_num}")
