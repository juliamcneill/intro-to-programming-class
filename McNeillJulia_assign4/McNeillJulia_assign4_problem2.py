"""
McNeillJulia_assign4_problem2

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 6 October, 2019 
"""
import random

#ask user how many sides are on their dice
sides = int(input('How many sides on your dice (4, 6, 8, 10, 12 or 20)? '))

#ensure that the user has picked a valid dice, and reprompt them if necessary
while sides not in {4, 6, 8, 10, 12, 20}:
    print("Sorry, that's not a valid size.")
    print()
    sides = int(input('How many sides on your dice (4, 6, 8, 10, 12 or 20)? '))

print()

print('Thanks! Here we go ...')

print()

#set starting variables
number_of_tries = 0
double_count= 0
die1 = 0
die2 = 0
sum1 = 0
sum2 = 0

#while the dice haven't hit snake eyes yet
while die1 != 1 or die2 != 1:
    #generate random integers for each die
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)
    #add one to double counter if they are doubles
    if (die1 == die2):
        double_count += 1
    #updates sum for each die
    sum1 += die1
    sum2 += die2
    #update number of tries
    number_of_tries += 1
    #print the dice roll
    print(str(number_of_tries) + '. Die number 1 is ' + str(die1) + ' and Die number 2 is ' + str(die2) + '.')

#when the dice hit snake eyes
number_of_tries += 1
    
#calculate percentage of doubles and average for each dice
double_percentage = double_count / number_of_tries
average_a = sum1 / (number_of_tries)
average_b = sum2 / (number_of_tries)

print()

#print results
print('You got snake eyes! Finally! On try number ' + str(number_of_tries) + '!')
print('Along the way you rolled doubles ' + str(double_count) + ' times (' + str(format(double_percentage, '.2%')) + ' of all rolls were doubles)')
print('The average roll for die #1 was', str(format(average_a, '.2')))
print('The average roll for die #2 was', str(format(average_b, '.2')))




