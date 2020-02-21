"""
McNeillJulia_assign3_problem2

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 29 September, 2019
"""
#import random and request a random number between 1 and 10
import random
number = random.randint(0, 10)

#ask the user to guess a number, and input that number as an integer
print("I'm thinking of a number between 1 and 10!")
guess = int(input("What's your guess? "))

#if the user guesses the number on the first try:     
if guess == number:
    print('You got it!')
    print('The secret number was ' + str(number) + '.')
    print('It took you 1 try to guess the number.')
#if the user does not guess the number on the first try
else:
    if guess < number:
        print('Too low, try again.')
        guess = int(input("What's your guess? "))
    else:
        print('Too high, try again.')
        guess = int(input("What's your guess? "))
#if the user guesses the number on the second try: 
    if guess == number:
        print('You got it!')
        print('The secret number was ' + str(number) + '.')
        print('It took you 2 tries to guess the number.')
#if the user does not guess the number on the second try: 
    else:
        if guess < number:
            print('Too low, try again.')
            guess = int(input("What's your guess? "))
        else:
            print('Too high, try again.')
            guess = int(input("What's your guess? "))
#if the user guesses the number on the third try: 
        if guess == number:
            print('You got it!')
            print('The secret number was ' + str(number) + '.')
            print('It took you 3 tries to guess the number.')
#if the user does not guess the number on the third try: 
        else:
            print("You didn't guess the number.")
            print('The secret number was ' + str(number) + '.')

            

