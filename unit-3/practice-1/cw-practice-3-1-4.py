"""
Author: Christine Wei
Date: March 20, 2023,
Description: Program that displays smallest and largest number in the file numbers.txt
"""

# opens numbers file
num_file = open('numbers.txt', 'r')

# sets smallest and largest integer equal to the first line in numbers.txt file
smallest = int(num_file.readline().strip())
largest = smallest

# for loop iterates through every number in numbers.txt
for line in num_file:
    num = int(line.strip())

    # if the number is less than the smallest, it becomes the new smallest
    if num < smallest:
        smallest = num
    # if the number is more than the largest, it becomes the new largest
    elif num > largest:
        largest = num
    # if they are equal, nothing changes
    else:
        continue

# displays largest and smallest number
print(f"""The smallest number is: {smallest}
The largest number is: {largest}""")

# closes number.txt file
num_file.close()
