"""
McNeillJulia_assign5_part2a

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 22 October, 2019
"""
#prompt user to enter positive integer to test
while True:
    integer = int(input('Enter a positive integer to test: '))
#validate that integer is positive
    if integer > 0:
        break
    print('That integer is not positive.')

print()

#set starting boolean value for prime number
prime_number = True

#one is not a prime number
if integer == 1:
    print(str(integer) + ' is not a prime number')
#two is a prime number
elif integer == 2:
    print(str(integer) + ' is a prime number')
#use a for loop to test for all integers over 2
else:
    for i in range(2, integer):
#break when you find a divisor
        if (integer % i == 0):
            print(str(i) + ' is a divisor of ' + str(integer) + ' ... stopping')
            prime_number = False
            break
#else, continue testing until you find a divisor or reach the user's integer
        else:
            print(str(i) + ' is NOT a divisor of ' + str(integer) + ' ... continuing')
    print()

#print results
    if (prime_number == True):
        print(str(integer) + ' is a prime number!')
    else:
        print(str(integer) + ' is not a prime number.')

