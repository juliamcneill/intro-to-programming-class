"""
McNeillJulia_assign4_problem1

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 6 October, 2019
"""
import turtle
import random

#ask user how many sides they want their shape to be
number_of_sides = int(input('How many sides? (Enter a number between 3 and 12, inclusive): '))

#ensure that the user picked number of sides is between 3 and 12, and reprompt them if necessary
while number_of_sides < 3 or number_of_sides > 12:
    print('That is out of range. Try again.')
    number_of_sides = int(input('How many sides? (Enter a number between 3 and 12, inclusive): '))

#set up our turtle window, pen color, and pen size
turtle.setup(600,600)
turtle.pencolor("black")
turtle.pensize(5)

#set numerical constants for shape
sum_of_angles = 360
length_of_window = 600
each_angle = sum_of_angles / number_of_sides
length_of_side = length_of_window / number_of_sides

#set counter for how many sides have been made
side_counter = 0

#move turtle to starting point
turtle.penup()
turtle.goto(-length_of_side/2,-length_of_side/2)
turtle.pendown()

#draw sides of turtle
while side_counter < number_of_sides:
    turtle.forward(length_of_side)
    turtle.left(each_angle)
    side_counter += 1

#hide turtle pointer
turtle.hideturtle()



    


