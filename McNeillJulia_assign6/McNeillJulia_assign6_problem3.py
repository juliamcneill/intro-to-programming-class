"""
McNeillJulia_assign6_problem3

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 29 October, 2019
"""
#import num_stats document
from McNeillJulia_num_stats import is_odd, is_even, is_prime, is_perfect, is_abundant

while True:
#introduce program
    print('Chart all even, odd, prime, perfect and abundant numbers within a given range.')
#ask user if they are ready to study
    ready = input('Ready? (Enter Y or y to continue; any other value to quit.) ')
    print()
#end program is user does not wish to continue
    if ready != 'y' and ready != 'Y':
        print("Goodbye!")
        break
    else:
        while True:
#if user is ready to start, ask them for starting number
            starting_number = int(input("Enter starting number (positive only): "))
#validate starting number, and reprompt if number is not valid
            if(starting_number < 0):
                print("Invalid, try again")
            else:
                break
        while True:
#ask user for ending number
            ending_number = int(input("Enter ending number (positive only): "))
#validate ending number, and reprompt if number is not valid
            if(starting_number < ending_number):
                break
            else:
                print("Invalid, try again")
  
#print the output
        print()
        print()
        print()
#print column headers, creating a column of width 10 for each
        print('{0:^10}'.format('Number'), end='')
        print('{0:^10}'.format('Even'), end='')
        print('{0:^10}'.format('Odd'), end='')
        print('{0:^10}'.format('Prime'), end='')
        print('{0:^10}'.format('Perfect'), end='')
        print('{0:^10}'.format('Abundant'))

#iterate through each number in the range
#fill in x for each function that returns True
#fill in a blank space for each function that returns False
        for number in range(starting_number, ending_number + 1):
            print('{0:^10}'.format(number), end='')
            if is_even(number):
                print('{0:^10}'.format('x'), end='')
            else:
                print('{0:^10}'.format(' '), end='')
            if is_odd(number):
                print('{0:^10}'.format('x'), end='')
            else:
                print('{0:^10}'.format(' '), end='')
            if is_prime(number):
                print('{0:^10}'.format('x'), end='')
            else:
                print('{0:^10}'.format(' '), end='')
            if is_perfect(number):
                print('{0:^10}'.format('x'), end='')
            else:
                print('{0:^10}'.format(' '), end='')
            if is_abundant(number):
                print('{0:^10}'.format('x'))
            else:
                print('{0:^10}'.format(' '))
        print()
        print()
        
