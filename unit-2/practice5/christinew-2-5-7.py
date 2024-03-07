"""
Author: Christine Wei
Date: 28/02/22
Description: Program simulates a fortune cookie. \
The program displays five unique fortunes, \
at random, each time it's run.
"""

import random

fortune1 = "You will be rich!"
fortune2 = "You will get good marks!"
fortune3 = "You will do well on your test!"
fortune4 = "You will not eat anything tasty today!"
fortune5 = "You will like cats more than dogs in 5 years"


def fortune(f1, f2, f3, f4, f5):
    print("Here are your fortune cookies!")
    for fortune in range(0, 5):
        picked_cookies = random.randint(1, 5)
        if picked_cookies == 1:
            print(fortune1)
        elif picked_cookies == 2:
            print(fortune2)
        elif picked_cookies == 3:
            print(fortune3)
        elif picked_cookies == 4:
            print(fortune4)
        elif picked_cookies == 5:
            print(fortune5)


fortune(fortune1, fortune2, fortune3, fortune4, fortune5)
