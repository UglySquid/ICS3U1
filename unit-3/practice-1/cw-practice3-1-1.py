"""
Author: Christine Wei
Date: March 20, 2023,
Description: Program that determines if the user's favorite fruit is in the list of groceries
"""

# asks user for their favorite fruit
fav_fruit = input("What's your favorite fruit? ")

# opens groceries file in read mode
groceries = open('groceries.txt', 'r')

# for loop that iterates through every line in groceries file
for line in groceries:
    # if the user's favorite fruit
    if groceries.readline().strip() == fav_fruit:
        # prints that the fruit is in the list and ends loop
        print("Your fruit is in the groceries!")
        break
    else:
        # prints that the fruit is not in the list and ends loop
        print("Your fruit is not the groceries! Sorry!")
        break

# closes groceries file
groceries.close()
