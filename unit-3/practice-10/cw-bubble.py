"""
Author: Christine Wei
Date: April 6, 2023,
Description: Improved bubble sort algorithm
"""

# This is the original, unsorted list
num_list = [4, 2, 5, 1, 3]
print("Original num_list is", num_list)

# Boolean flag is initialized as false, assumes that the list is sorted
swap = False

# Outer loop iterates through every value in list
for pass_num in range(1, len(num_list)):
    for index in range(len(num_list) - 1):
        if num_list[index] > num_list[index + 1]:
            temp = num_list[index]
            num_list[index] = num_list[index + 1]
            num_list[index + 1] = temp
            # If a swap occurred, swap becomes True
            swap = True

    # If the swap never occurred in the inner loop, it breaks the outer loop
    if not swap:
        break

    # (Optional) Display the list after each pass
    print("After Pass #", pass_num, "num_list is", num_list)
    print("The sorted list is: ", num_list)
