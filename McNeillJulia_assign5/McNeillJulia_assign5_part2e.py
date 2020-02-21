"""
McNeillJulia_assign5_part2e

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
print('All primes between ' + str(start_of_range) + ' and ' + str(end_of_range) + ':')

#set count of prime numbers
prime_number_count = 0

#set first divisor to test whether each number is prime
first_divisor = 2

#test each number after 1
for integer in range(start_of_range, end_of_range + 1):
    if integer > 1:
        sqrt_integer = int(integer ** (1/2))
#test each number repeating with divisor and break if it isn't prime
#here, instead of testing until the integer itself becomes the divisor,
#i've tested until the square root of the integer becomes the divisor,
#which is the highest number that must be tested to check if the number
#is prime or not. this makes the execution time longer for smaller
#ranges of numbers, because of the extra calculation involved to find
#the square root of each integer, but makes the execution time shorter
#for larger ranges of numbers, because as the numbers get larger, you
#can save more time by testing less numbers as divisors on each integer
        for divisor in range(first_divisor, sqrt_integer):
            if (integer % divisor == 0):
                break
#add to prime count and print results if number is prime
        else:
            prime_number_count += 1
            if (prime_number_count % 10 == 0):
#add necessary number of spaces to fit in different lengths of numbers
                if end_of_range > 999:
                    print("%6d" % integer)
                elif end_of_range > 99:
                    print("%3d" % integer)
                else:
                    print("%d" % integer)
            else:
                if end_of_range > 999:
                    print("%6d" % integer, end=" ")
                elif end_of_range > 99:
                    print("%3d" % integer, end=" ")
                else:
                    print("%d" % integer, end=" ")

#set ending time
end_time = time.time()

#print execution time
print()
print('Execution time: ' + str(format(end_time - start_time, '.3f')) + ' seconds.')



