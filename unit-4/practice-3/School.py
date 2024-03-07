"""
Author: Christine Wei
Date: April 21, 2023,
Description: School module
"""


class Teacher(object):
    def __init__(self):
        self.__name = "Ms. Huynh"
        self.__mood = "content"

    def __str__(self):
        return f"{self.__name} is {self.__mood}"

    def get_name(self):
        return self.__name

    def get_mood(self):
        return self.__mood

    def catch_late_student(self):
        self.__mood = "unhappy"

    def mark_good_test(self):
        self.__mood = "delighted"