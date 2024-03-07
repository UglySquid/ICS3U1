"""
Author: Christine Wei
Date: April 19, 2023,
Description: Ms. Huynh's moods
"""


class Teacher(object):
    def __init__(self):
        self.name = "Ms. Huynh"
        self.mood = "content"

    def get_name(self):
        return self.name

    def get_mood(self):
        return self.mood

    def catch_late_student(self):
        self.mood = "unhappy"

    def mark_good_test(self):
        self.mood = "delighted"


def main():
    huynh = Teacher()

    print(huynh.get_name(), "is", huynh.get_mood())
    print("\nOh no, a student just came in late!")
    huynh.catch_late_student()

    # huynh.mood = "thrilled!"
    print(huynh.get_name(), "is", huynh.get_mood())
    print("\nGreat, we just aced our test!")
    huynh.mark_good_test()
    print(huynh.get_name(), "is", huynh.get_mood())

    print("\nMs. Huynh's mood is", huynh.get_mood())
    huynh.mood = "VERY VERY VERY HAPPY"
    print("Ms. Huynh's mood is", huynh.get_mood())


main()
