"""
McNeillJulia_assign6_problem1

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 29 October, 2019
"""
# function:   compute_area_of_rectangle
# input:      length (integer) and width (integer)
# processing: computes the area of the described rectangle
# output:     returns the area of the described rectangle (integer)
def compute_area_of_rectangle(length, width):
    return length * width

# function:   compute_perimeter_of_rectangle
# input:      length (integer) and width (integer)
# processing: computes the perimeter of the described rectangle
# output:     returns the perimeter of the described rectangle (integer)
def compute_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# function:   draw_rectangle
# input:      length (integer) and width (integer)
# processing: constructs the rectangle using a series of "*" characters (see below for a sample 4 by 3 rectangle:)
#             ***
#             ***
#             ***
#             ***
# output:     returns the rectangle (string)
def draw_rectangle(length, width):
#create variable to be returned
    rectangle = ""
#add symbols to variable using a for loop for both length and width
    for lengths in range(length):
        for widths in range(width):
            rectangle += "*"
#stay on same line within each length row
        rectangle += "\n"

    return rectangle

# function:   get_input
# input:      a prompt to ask the user (String), a low value (integer) and a high value (integer)
# processing: prompts the user for integer input, using the supplied prompt. if the user does not supply
#              an integer within the specified range the function will re-prompt them until they do
# output:     returns the integer the user supplied
def get_input(prompt, low_value, high_value):
#validate that input is within the right range used as input for the function
    while True:
        user_value = int(input(prompt + ": "))
        if user_value >= low_value and user_value <= high_value:
            return user_value
        else:
            print("Sorry! That's an invalid input.")

#call functions to prompt user for input
length = get_input("Enter a length between 3 and 10", 3, 10)
width  = get_input("Enter a width between 3 and 10", 3, 10)

#call functions to compute area and perimeter of rectangle
area  = compute_area_of_rectangle(length, width)
perim = compute_perimeter_of_rectangle(length, width)

#print area and perimeter
print ("Area:", area, "; Perim:", perim)

#call function to draw rectangle and print return variable of function
rect = draw_rectangle(length, width)
print (rect)
