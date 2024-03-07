"""
Author: Christine Wei
Date: 28/02/22
Description: Program displays table that shows Fahrenheit temperatures \
and their corresponding Celsius temperatures
"""


def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32) * (5.0 / 9.0)


def temperature_table():
    print("Fahrenheit | Celsius")
    for temp in range(0, 21):
        temp_c = round(fahrenheit_to_celsius(temp), 1)
        print(temp, "|", temp_c)


temperature_table()
