"""
McNeillJulia_assign5_part2c

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 22 October, 2019
"""
import time

#prompt user to enter start and end of range
while True:
    start_of_range = int(input('Start number: '))
    end_of_range = int(input('End number: '))
#validate that both start and end of range are positive
    if start_of_range and end_of_range > 0:
#validate that end of range is greater than start of range
        if end_of_range > start_of_range:
            break
        else:
            print('End number must be greater than start number')
            print()
    else:
        print('Start and end must be positive')
        print()

print()

#set starting time
start_time = time.time()

#print range
print('The prime numbers between ' + str(start_of_range) + ' and ' + str(end_of_range) + ' are:')

#set count of prime numbers
prime_number_count = 0

#set first divisor to test whether each number is prime
first_divisor = 2

#test each number after 1
for integer in range(start_of_range, end_of_range + 1):
    if integer > 1:
#test each number repeating with divisor and break if it isn't prime
        for divisor in range(first_divisor, integer):
            if (integer % divisor == 0):
                break
#add to prime count and print results if number is prime
        else:
            prime_number_count += 1
            print(integer)

#set ending time
end_time = time.time()

#print overall results
print('Found ' + str(prime_number_count) + ' prime numbers.')
print('Execution time: ' + str(format(end_time - start_time, '.2f')) + ' seconds.')



