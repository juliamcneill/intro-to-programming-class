"""
McNeillJulia_assign3_problem1

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 29 September, 2019
"""
#import turtle for the extra credit
import turtle

#display title
print('Valid Triangle Tester')

print()

#prompt user to enter x and y coordinates for 3 points
point1_x = float(input('Enter Point #1 - x position: '))
point1_y = float(input('Enter Point #1 - y position: '))
point2_x = float(input('Enter Point #2 - x position: '))
point2_y = float(input('Enter Point #2 - y position: '))
point3_x = float(input('Enter Point #3 - x position: '))
point3_y = float(input('Enter Point #3 - y position: '))

#calculate each side of the triangle using the distance formula
side1 = ((point1_x - point2_x)**2 + (point1_y - point2_y)**2)**(.5)
side2 = ((point2_x - point3_x)**2 + (point2_y - point3_y)**2)**(.5)
side3 = ((point3_x - point1_x)**2 + (point3_y - point1_y)**2)**(.5)

print()

#round each side of the triangle to two decimal places
side1 = round(side1, 2)
side2 = round(side2, 2)
side3 = round(side3, 2)

#set up our turtle window, pen color, and pen size
turtle.setup(250,250)
turtle.pencolor("black")
turtle.pensize(5)

#display the length of each side of the triangle
print('The length of each side of your test shape is: ')

print()

print('Side 1: ' + format(side1, '.2f'))
print('Side 2: ' + format(side2, '.2f'))
print('Side 3: ' + format(side3, '.2f'))

print()

#calculate and display whether the triangle is valid or not
if (side1 + side2) > side3 and (side2 + side3) > side1 and (side3 + side1) > side2:
    print('This is a valid triangle!')
#if the triangle is valid, calculate and display what kind of triangle it is
#set the turtle fill color accordingly
    if side1 == side2 == side3:
        print('This is an equilateral triangle')
        turtle.fillcolor("blue")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print('This is an isosceles triangle')
        turtle.fillcolor("yellow")
    else:
        print('This is an scalene triangle')
        turtle.fillcolor("green")
else:
    print('This is not a valid triangle')

#draw the triangle using turtle
turtle.penup
turtle.goto(point1_x, point1_y)
turtle.pendown
turtle.begin_fill()
turtle.goto(point2_x, point2_y)
turtle.goto(point3_x, point3_y)
turtle.goto(point1_x, point1_y)
turtle.end_fill()

