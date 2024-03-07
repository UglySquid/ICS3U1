"""
Author: Christine Wei
Date: 28/02/22
Description: Program that repeatedly prompts the user to enter a number and then displays a message \
indicating whether the number is prime or not.\
If the user enters a zero (0) the program should stop.
"""


def main():
    while True:
        number = int(input("Give me a number, enter 0 to stop: "))
        if number == 0:
            break
        prime = is_prime(number)
        if not prime:
            print("Not a prime number.")
        else:
            print("Prime number.")
            continue


def is_prime(num):
    if num == 1:
        return True
    else:
        for factor in range(2, num+1):
            if (num % factor) == 0 and num != factor:
                return False
            else:
                return True


main()
