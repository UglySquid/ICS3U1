"""
Author: Christine Wei
Date: 28/02/22
Description: Program simulates rolling a die 1000 times
"""

import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

print("Rolling dice...")
for x in range(1, 1001):
    num_roll = random.randint(1, 6)
    if num_roll == 1:
        one += 1
    elif num_roll == 2:
        two += 1
    elif num_roll == 3:
        three += 1
    elif num_roll == 4:
        four += 1
    elif num_roll == 5:
        five += 1
    else:
        six += 1

print(f"The final counts are: \n"
      f"{one} ones \n"
      f"{two} twos \n"
      f"{three} threes \n"
      f"{four} fours \n"
      f"{five} fives \n"
      f"{six} sixes \n")