"""
McNeillJulia_assign2_problem3

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 22 September, 2019 
"""
import math

# prompt user to enter all necessary input
print("Hello! I'm here to help you calculate your tip.")
bill_without_tip = float(input('How much was your bill? (Enter a numeric value without commas or dollar signs): '))
tip_integer = int(input('How much tip would you like to leave? (A percentage: enter an integer value - i.e. 15 = 15%): '))
number_of_people = int(input('How many individuals are splitting the bill? (Enter an integer value): '))

# convert tip to decimal
tip_percentage = tip_integer / 100

# originally i used tip_amount = bill_without_tip * tip_percentage, however this creates a logic error
# in which the tip amount may be rounded down when divided up between each individual. this solution uses math.ceil
# to round the tip_amount up to the nearest cent. you must multiply by 100, use math.ceil, and then divide by 100
# because math.ceil only outputs integers
tip_amount = math.ceil((bill_without_tip * tip_percentage * 100.0)) / 100.0

# add the tip to the original bill amount to produce the new bill amount, with tip
bill_with_tip = bill_without_tip + tip_amount

# divide the new bill amount by the number of people. use math.ceil again to ensure that the tip is not underestimated
# when the final amount is divided between the number of people and rounded
split_bill = math.ceil((bill_with_tip / number_of_people * 100.0)) / 100.0

print()

# displays waiting message to user
print('Thanks!  Calculating your bill & tip ...')

# displays final amounts to user, making sure to display each amount with two decimal places
print('You need to leave $' + str(format(tip_amount, ".2f")), 'as a tip.')
print('Your total bill will be $' + str(format(bill_with_tip, ".2f")) + '.')
print('Each individual should pay $' + str(format(split_bill, ".2f")) + '.')
