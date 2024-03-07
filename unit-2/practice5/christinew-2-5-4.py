"""
Author: Christine Wei
Date: 28/02/22
Description: Program that prompts the user to enter three numbers, then displays the greatest of the three.
"""


def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))

    max_num = maximum(number1, number2, number3)
    print(max_num)


def maximum(num1, num2, num3):
    greatest_num = num1
    if greatest_num < num2:
        greatest_num = num2
    if greatest_num < num3:
        greatest_num = num3

    return greatest_num


main()
