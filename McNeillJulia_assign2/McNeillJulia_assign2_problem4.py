"""
McNeillJulia_assign2_problem4

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 22 September, 2019 
"""
import math

# print description of use for program
print('Minecraft block distance calculator')

print()

# have user enter the x, y, and z values of two blocks
block1_x_value = int(input('Block #1 x: '))
block1_y_value = int(input('Block #1 y: '))
block1_z_value = int(input('Block #1 z: '))
block2_x_value = int(input('Block #2 x: '))
block2_y_value = int(input('Block #2 y: '))
block2_z_value = int(input('Block #2 z: '))

print()

# this next section determines how to find the distance between
# two blocks and then calculates the distance accordingly

# if the blocks both have positive x values, we should determine
# which value is smaller and subtract that value from the larger
if block1_x_value > 0 and block2_x_value > 0:
    if block1_x_value > block2_x_value:
        x_distance = block1_x_value - block2_x_value
    else:
        x_distance = block2_x_value - block1_x_value
# if the blocks both have negative x values, we should determine
# which value is small and subtract that value from the larger
elif block1_x_value < 0 and block2_x_value < 0:
    if block1_x_value > block2_x_value:
        x_distance = block1_x_value - block2_x_value
    else: 
        x_distance = block2_x_value - block1_x_value
# if one block has a positive x value, and one has a negative x
# value, we should add the absolute value of each value
else: 
    x_distance = abs(block1_x_value) + abs(block2_x_value)

# the same logic applies to both y and z values, below
if block1_y_value > 0 and block2_y_value > 0:
    if block1_y_value > block2_y_value:
        y_distance = block1_y_value - block2_y_value
    else:
        y_distance = block2_y_value - block1_y_value
elif block1_y_value < 0 and block2_y_value < 0:
    if block1_y_value > block2_y_value:
        y_distance = block1_y_value - block2_y_value
    else:
        y_distance = block2_y_value - block1_y_value
else: 
    y_distance = abs(block1_y_value) + abs(block2_y_value)


if block1_z_value > 0 and block2_z_value > 0:
    if block1_z_value > block2_z_value:
        z_distance = block1_z_value - block2_z_value
    else:
        z_distance = block2_z_value - block1_z_value
elif block1_z_value < 0 and block2_z_value < 0:
    if block1_z_value > block2_z_value:
        z_distance = block1_z_value - block2_z_value
    else:
        z_distance = block2_z_value - block1_z_value
else: 
    z_distance = abs(block1_z_value) + abs(block2_z_value)

# print the distance between the x values, y values, and z values
print('X distance: ' + str(x_distance))
print('Y distance: ' + str(y_distance))
print('Z distance: ' + str(z_distance))

# calculate the straight line distance by inputting the user's
# values into the 3d distance formula
straight_line_distance = (((block2_x_value - block1_x_value) ** 2) + ((block2_y_value - block1_y_value) ** 2) + ((block2_z_value - block1_z_value) ** 2)) ** 0.5

# print the straight line distance, to two decimal places
print('Straight line distance: ' + str(format(straight_line_distance, ".2f")))
    
