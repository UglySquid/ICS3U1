"""
Author: Christine Wei
Date: March 6, 2023,
Description:
asks for 5 integer test scores
displays letter grade for each test score
displays average test score
"""

# imports the grading module
import grading


# mainline logic
def main():
    """
    Asks user for 5 scores
    Calculates the 5 grades for the 5 scores
    Calculates the average of the 5 scores
    Displays the 5 grade and the average of the 5 scores
    """

    # asks user to input 5 scores
    score1 = int(input("Score #1: "))
    score2 = int(input("Score #2: "))
    score3 = int(input("Score #3: "))
    score4 = int(input("Score #4: "))
    score5 = int(input("Score #5: "))

    # calculates grades
    grade1 = grading.determine_grade(score1)
    grade2 = grading.determine_grade(score2)
    grade3 = grading.determine_grade(score3)
    grade4 = grading.determine_grade(score4)
    grade5 = grading.determine_grade(score5)

    average = grading.calc_average(score1, score2, score3, score4, score5)

    # displays grades
    print("Grade #1: ", grade1)
    print("Grade #2: ", grade2)
    print("Grade #3: ", grade3)
    print("Grade #4: ", grade4)
    print("Grade #5: ", grade5)

    # displays average
    print("\nYour average is: ", round(average, 1))


main()
