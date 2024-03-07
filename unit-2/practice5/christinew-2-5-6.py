"""
Author: Christine Wei
Date: 28/02/22
Description: displays all prime numbers from 1 to 100
"""


def main():
    for num in range(1, 101):
        if is_prime(num) == True:
            print(num)
        else:
            continue


def is_prime(num):
    if num == 1:
        return True
    else:
        for factor in range(2, num + 1):
            if (num % factor) == 0 and num != factor:
                return False
            else:
                return True


main()
