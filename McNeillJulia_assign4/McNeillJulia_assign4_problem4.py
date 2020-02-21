"""
McNeillJulia_assign4_problem2

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 6 October, 2019 
"""
import random
import time

#prompt user to enter number of throws
throw_count_input = int(input('How many throws would you like to simulate? '))

#ensure that number of throws is greater than zero
while throw_count_input <= 0:
    print("Sorry, try again.")
    throw_count_input = int(input('How many throws would you like to simulate? '))

#begin time
start_time = time.time()

#begin accumulators
points0 = 0
points10 = 0
points20 = 0
points30 = 0
points40 = 0
throw_count = 0

#loop reiterates until throw count tracker is one lower than the throw count input by the user
while throw_count < throw_count_input:
    #add one to throw tracker
    throw_count += 1
    #generate random positions
    ball_x = random.uniform(0,48)
    ball_y = random.uniform(0,60)
    #checks if ball lands in big circle
    if (24 - ball_x) ** 2 + (38 - ball_y) ** 2 <= 18 ** 2:
        #checks if ball lands in 20 point circle
        if (24 - ball_x) ** 2 + (38 - ball_y) ** 2 <= 6 ** 2:
            points20 += 1
        #checks if ball lands in 30 point circle
        elif (24 - ball_x) ** 2 + (26 - ball_y) ** 2 <= 5 ** 2:
            points30 += 1
        #all other balls in big circle are outside smaller circles and are 10 points
        else:
            points10 += 1
    #checks if ball lands in 40 point circle
    elif (24 - ball_x) ** 2 + (5 - ball_y) ** 2 <= 4 ** 2:
        points40 += 1
    #all other balls have missed the circles completely and are 0 points
    else:
        points0 += 1

#end time
end_time = time.time()

#calculate execution time
execution_time = end_time - start_time

#calculate throw percentage
throws_percentage = throw_count/throw_count

#calculate percent of total throws for each ring
points0_percentage = points0 / throw_count
points10_percentage = points10 / throw_count
points20_percentage = points20 / throw_count
points30_percentage = points30 / throw_count
points40_percentage = points40 / throw_count

#let user know that program is finished
print()
print("Done!")

#display execution time
print("Execution time:", format(execution_time, '.2f'), 'seconds')

print()

#display total throws
print("* Total throws:\t", format(throw_count, ">9,") + format(throws_percentage, ">9.2%"))
#display misses
print("* Misses:\t", format(points0,'>9,')  + format(points0_percentage, '>9.2%'))
#display counts and percentages for each ball made in a hole
print("* 10 points:\t", format(points10,'>9,')  + format(points10_percentage, '>9.2%'))
print("* 20 points:\t", format(points20,'>9,')  + format(points20_percentage, '>9.2%'))
print("* 30 points:\t", format(points30,'>9,')  + format(points30_percentage, '>9.2%'))
print("* 40 points:\t", format(points40,'>9,')  + format(points40_percentage, '>9.2%'))



