"""
Author: Christine Wei
Date: 28/02/22
Description: Program displays table that shows Fahrenheit temperatures \
and their corresponding Celsius temperatures
"""


def main():
    min_temp, max_temp = int(input("Input lowest temp: ")), int(input("Input highest temp: "))
    temperature_table(min_temp, max_temp)


def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32) * (5.0 / 9.0)


def temperature_table(min_val, max_val):
    print("Fahrenheit | Celsius")
    for temp in range(min_val, max_val+1):
        temp_c = round(fahrenheit_to_celsius(temp), 1)
        print(temp, "|", temp_c)


main()
