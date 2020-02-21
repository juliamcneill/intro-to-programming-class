"""
McNeillJulia_assign5_part2b

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 22 October, 2019
"""
import time

#set starting time
start_time = time.time()
#set count of prime numbers
prime_number_count = 0

#set start and end of testing range
start_of_range = 1
end_of_range = 1000
#set first divisor to test whether each number is prime
first_divisor = 2

#print result for 1
print('1 is technically not a prime number.')

#test each number after 1
for integer in range(start_of_range, end_of_range):
    if integer > 1:
#test each number repeating with divisor and break if it isn't prime
        for divisor in range(first_divisor, integer):
            if (integer % divisor == 0):
                break
#add to prime count and print results if number is prime
        else:
            prime_number_count += 1
            print(str(integer) + ' is a prime number!')

#set ending time
end_time = time.time()

#print overall results
print('Found ' + str(prime_number_count) + ' prime numbers between 1 and 1000.')
print('Execution time: ' + str(format(end_time - start_time, '.2f')) + ' seconds.')



