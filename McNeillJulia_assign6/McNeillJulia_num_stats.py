"""
McNeillJulia_num_stats

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 29 October, 2019
"""
# is_odd
# Input: number (int)
# Processing: Test to see if that number is odd
# Output: True if it is odd, False otherwise (boolean)
def is_odd(number):
    return number % 2 == 1

# function:   is_even
# input:      a positive integer
# processing: determines if the supplied number is even
# output:     boolean
def is_even(number):
    return number % 2 == 0

# is_prime
# Input: number (int)
# Processing: Test to see if that number is prime
# Output: True if it is prime, False otherwise (boolean)
def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False   
    return True

# is_square
# Input: number (int)
# Processing: Test to see if that number is a perfect square. 
# Output: True if it is a perfect square, False otherwise (boolean)
def is_square(number):
#find the square root with a decimal
    square_root_float = number**0.5
#find the square root without a decimal
    square_root_int = int(square_root_float)
#determine whether the decimal is 0 or not
    return abs(square_root_float - square_root_int) == 0 

# length
# Input: number (int)
# Processing: Count the number of digits in int
# Output: The number of digits in int
#assumes the length is less than 1000
def length(number):
    for i in range(1,1000):
        if number >= 10**i:
            continue
        else:
            return i

# function:   is_perfect
# input:      a positive integer
# processing: determines if the supplied number is perfect. a perfect number
#             is a number that is equal to the sum of its factors besides itself
#             (i.e. the number 6 is perfect because 6 = 1 + 2 + 3)
# output:     boolean
def is_perfect(number):
    if number == 1:
        return False
    sum_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_factors += i
    return sum_factors == number

# function:   is_abundant
# input:      a positive integer
# processing: determines if the supplied number is abundant. an abundant number
#             is a number that is less than the sum of its factors besides itself
#             (i.e. the number 12 is abundant because 12 < 1 + 2 + 3 + 4 + 6)
# output:     boolean
def is_abundant(number):
    if number == 1:
        return False
    sum_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_factors += i
    return sum_factors > number
