"""
Author: Christine Wei
Date: 27/02/22
Description:
Loop that calculates the (float) sum of the following series of numbers:
1/10 + 2/9 + 3/8 + ... + 10/1
"""

sum = 0

for numerator in range(1, 11):
    num = float(numerator)
    denominator = 11.0 - numerator
    sum += num/denominator

print(sum)
