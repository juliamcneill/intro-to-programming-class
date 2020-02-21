"""
McNeillJulia_assign2_problem1

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 22 September, 2019
"""
import math

# announce what the program is for
# print(Circle Analyzer)
# syntax error, we must enclose Circle Analyzer in quotes because it is a string
print('Circle Analyzer')

# define the named constant pi
# logic error, we have not defined the named constant pi
pi = 3.14159

# get the diameter 
# diameter = input("Enter the diameter of the circle: )
# syntax error, we must close the string with a second quote
# logic error, we must convert what the user enters into a float
diameter = float(input('Enter the diameter of the circle: '))

# compute the area
# area = pi * diameter / 2 ** 2
# syntax error, missing parenthesis
# logic error, we have not defined the named constant pi
# logic error, we have not placed commas to clarify order of operations
area = pi * ((diameter / 2) ** 2)

# print the output
# logic error, for all outputs, there should be three decimal places
# logic error, for all outputs of floats, there should be an f at the end of the format specifier

# print(format("Diameter:","<14"),format(diameter,">7.3d")
# syntax error, we must close the parenthesis that opens after print
# logic error, d is used to format integers, and this is a float
print(format("Diameter:","<14"),format(diameter,">7.3f"))
# print(format("Radius:","<14"),format(diameter//2,">7.3f"))
# logic error, we should use / instead of // because we want a decimal in the result
print(format("Radius:","<14"),format(diameter/2,">7.3f"))
# logic error, we have aligned Circumference to the right, instead of the left
# syntax error, we have not included the multiplication sign between pi and diameter
# logic error, we have not defined the named constant pi
# print(format("Circumference:",">14"),format(pidiameter,">7.3"))
print(format("Circumference:","<14"),format(pi * diameter,">7.3f"))
# print(format("Area:",format(area,">7.3"))
# logic error, we have not aligned Area to the right
print(format("Area:","<14"),format(area,">7.3f"))
