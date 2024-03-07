"""
Author: Christine Wei
Date: April 21, 2023,
Description: 3D Tic Tac Toe Game
"""

import School


def main():
    """
    Mainline logic to test School module
    """
    huynh = School.Teacher()

    print(huynh.get_name(), "is", huynh.get_mood())
    print("\nOh no, a student just came in late!")
    huynh.catch_late_student()

    huynh.mood = "thrilled!"
    print(huynh.get_name(), "is", huynh.get_mood())
    print("\nGreat, we just aced our test!")
    huynh.mark_good_test()
    print(huynh.get_name(), "is", huynh.get_mood())


main()
