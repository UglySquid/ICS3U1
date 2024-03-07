"""
Author: Christine Wei
Date: March 20, 2023,
Description: Program that determines if the user's favorite fruit is in the list of groceries.
If it isn't in the list, program will add user's favorite fruit to the groceries file
"""

# asks user for their favorite fruit
fav_fruit = input("What's your favorite fruit? ")

# opens groceries file in read mode
groceries = open('groceries.txt', 'r')

# opens groceries file in append mode
groceries_new = open('groceries.txt', 'a')

# for loop that iterates through every line in groceries file
for line in groceries:
    # if the fruit is in the groceries list, displays phrase that tells user that
    if line.strip() == fav_fruit:
        print("Your fruit is in the groceries!")
        break
    # if the fruit is not in groceries list, it appends the user's favorite fruit to the groceries list
    else:
        print("Your fruit is not the groceries! Sorry!")
        groceries_new.write(fav_fruit)
        break

# closes groceries files
groceries.close()
groceries_new.close()
