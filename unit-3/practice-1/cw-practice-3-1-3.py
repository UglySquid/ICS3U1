"""
Author: Christine Wei
Date: March 20, 2023,
Description: Program that checks if the user's disliked fruit is in groceries list.
If it is in list, program creates new file without the user's disliked fruit.
"""

# asks user that their disliked fruit is
dis_fruit = input("What's your disliked fruit? ")

# opens groceries file in read mode
groceries = open('groceries.txt', 'r')

# creates empty strings
old_groceries_list = ""
new_groceries_list = ""

# for loop that iterates through every line in groceries file
for line in groceries:
    # if line is not disliked fruit
    if line.strip() != dis_fruit:
        # add it to new groceries list
        new_groceries_list += line.strip()
        new_groceries_list += '\n'
        # add it to old groceries list
        old_groceries_list += line.strip()
        old_groceries_list += '\n'
    else:
        # add it to old groceries list
        old_groceries_list += line.strip()
        old_groceries_list += '\n'
        print("The fruit you dislike is in the grocery list. A new list has been created!")

# compares old groceries list and new groceries list
if old_groceries_list == new_groceries_list:
    # when the two lists are the same, disliked fruit is not in list and displays statement to tell user that
    print("The fruit you dislike is not in the grocery list, no worries!")
else:
    # when lists are different, creates new groceries list that does not include fruit the user dislikes
    groceries_new = open('groceries.new.txt', 'w')
    groceries_new.write(new_groceries_list)
    groceries_new.close()

# closes groceries file
groceries.close()
