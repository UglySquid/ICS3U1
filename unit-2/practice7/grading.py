"""
Author: Christine Wei
Date: March 6, 2023,
Description: Module with calc_average() and determine_grade() functions
"""


def calc_average(score1, score2, score3, score4, score5):
    # convert integer scores into float
    score1 = float(score1)
    score2 = float(score2)
    score3 = float(score3)
    score4 = float(score4)
    score5 = float(score5)

    # calculates the average of the 5 scores
    average = (score1 + score2 + score3 + score4 + score5)/5

    # returns average
    return average


def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
