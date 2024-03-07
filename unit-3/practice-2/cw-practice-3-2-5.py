"""
Author: Christine Wei
Date: March 21, 2023,
Description: sums and averages all the numbers in numbers.txt file
"""

numbers = open('numbers.txt', 'r')

# variable representing the sum of numbers in the file
num_sum = 0

# variable used to calculate line number
line_number = 0

# set the number of numbers to 0 to calculate average with
num_of_nums = 0

# initialize variable average
average = 0

# for loop that iterates through all lines in number file
for line in numbers:
    # changes line number to match each line for each iteration of for loop
    line_number += 1

    # try except to see if line is a number or string
    try:
        # if line is float value, number is added to sum of numbers
        num_sum += float(line.strip())
        # number of numbers increases by 1
        num_of_nums += 1
    except ValueError:
        # if line is something other than float value, it prints the line number and what is in the line
        print(f"#{num_of_nums} {line.strip()}")
        continue

# calculates the average of the numbers
average = num_sum/num_of_nums

# displays the sum and average of the numbers
print(f"""The sum is: {num_sum}
The average is: {average}""")
