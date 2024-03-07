
def main():
    """Takes in keyboard input from user, shows error message, runs rom_numer()"""
    while True:
        try:
            num = int(input("Please input a number from 1 to 10: "))
        except ValueError: 
            print("That's not a number!")
        else:
            if num>=1 and num<=10:
                rom_numeral(num)
            else:
                print("That number is not between 1 and 10, please try again!")
        
#converts from number to roman numeral and displays converted number
def rom_numeral(num):
    """Takes in number as integer, outputs roman numeral as string"""
    if num == 1:
        print("I")
    elif num == 2:
        print("II")
    elif num == 3:
        print("III")
    elif num == 4:
        print("IV")
    elif num == 5:
        print("V")
    elif num == 6:
        print("VI")
    elif num == 7:
        print("VII")
    elif num == 8:
        print("VIII")
    elif num == 9:
        print("IX")
    else:
        print("X")
        
main()



