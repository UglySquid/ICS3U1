# Asks user for length and width of their two rectangles
def main():
    """Takes keyboard input from user, outputs string statement that describes"""
    rect1_length = int(input("Input the length of the first rectangle:"))
    rect1_width = int(input("Input the width of the first rectangle:"))
    rect2_length = int(input("Input the length of the second rectangle:"))
    rect2_width = int(input("Input the width of the second rectangle:"))
    
    calculate_area(rect1_length, rect1_width, rect2_length, rect2_width)


# Calculates area of rectangles and runs display_comparison()
def calculate_area(rect1_length, rect1_width, rect2_length, rect2_width):
    """Takes lengths and widths of two rectangles as integer input, runs display_comaprison()"""
    area_1 = rect1_length*rect1_width
    area_2 = rect2_length*rect2_width
    
    display_comparison(area_1, area_2)


# Compares areas of two rectangles and displays statement that describes their relation
def display_comparison(area_1, area_2):
    """Takes in areas of two rectangeles as integer input, outputs string statement describing their relation"""
    if area_1 > area_2:
        print("The area of your first rectangle is larger than the area of your second rectangle")
    elif area_1 < area_2:
        print("The area of your second rectangle is larger than the area of your first rectangle")
    else:
        print("The area of your second rectangle the same as the area of your first rectangle")
        
main()
