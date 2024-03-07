"""
Author: Christine Wei
Date: 24/02/22
Description: Program that asks user for 10 numbers, \
keeps a count of all the numbers entered, \
two pennies the second day, \
and displays the total sum and average.
"""

count = 1
num_sum = 0

# For loop that iterates between numbers 1 to 10
for i in range(1, 11):
    # Asks user to input number from keyboard
    num = float(input(f"Enter number {count}: "))
    # Counter that counts number of iterations
    count += 1
    # Calculates the sum of all the numbers inputted
    num_sum += num

# Calculates the average of all the numbers inputted
average = num_sum/10

# Displays sum and average
print(f"\nThe sum is: {num_sum}")
print(f"\nThe average is: {average}")

    