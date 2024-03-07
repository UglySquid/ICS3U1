
"""
Author: Christine Wei
Date: 24/02/22
Description: Program that calculates the amount of money a person would earn over a period of time \
if his or her salary is one penny the first day, \
two pennies the second day, \
and continues to double each day.
"""

# Asks user to input number of days, calls calc_display_salary()
def main():
    num_days = int(input("Number of days worked: "))
    
    # Calls another function
    calc_display_salary(num_days)
        
def calc_display_salary(num_days):
    total = 0
    
    # Tells the program to iterate the number of days
    for day in range(1, num_days+1):
        total = 0 + 2**(day-1)
        print(f"Day {day}: ${total/100}")
    
    # Tells the user what their total pay is
    print("Your total pay was: ", total)

main()