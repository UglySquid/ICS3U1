"""
Author: Christine Wei
Date: March 30, 2023,
Description: Converts number format date into word format date
"""


def expand_date(original_date):
    """
    Accepts date as string in format mm/dd/yyyy
    Returns date as string in the format of Month, day, year (March 12, 2023)
    """

    # Splits the string into a list such that list resembles [month, day, year]
    new_date = original_date.split("/")

    # In the list of numbers representing the date, finds which number is month, day. year
    month = int(new_date[0])
    day = int(new_date[1])
    year = int(new_date[2])

    # List of months
    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]

    return f"{months[month-1]} {day}, {year}"
