"""
McNeillJulia_assign6_problem2

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 29 October, 2019
"""
#import sys to quit program if the user enters no valid numbers
import sys
#import num_stats document
from McNeillJulia_num_stats import is_odd, is_prime, is_square, length

#main function
def main():

#set up variables
    total_numbers = 0
    total_sum =  0
    shortest = 0
    longest = 0
    odds = 0
    evens = 0
    squares = 0
    primes = 0

#iterate through for each number that the user enters
    while True:
        number = input("Enter a positive integer (or 'end' to end): ")
#if user enters end
        if number == "end":
#show error message and end program if there are no valid numbers
            if total_numbers == 0:
                print()
                print("You entered no valid numbers.")
                sys.exit()
#exit While loop and proceed to displaying results
            else:
                break

#convert number to integer
        number = int(number)

#if number is less than 0, display error message and restart loop
        if number < 0:
            print("Invalid entry. Must be 0 or positive.")
            continue

#add 1 to total number count
        total_numbers += 1
#add number to total sum
        total_sum += number

#update largest, smallet, shortest, and longest on first loop
        if total_numbers == 1:
            largest = number
            smallest = number
            shortest = length(number)
            longest = length(number)
#update all tracking variables on each loop
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
        if shortest > length(number):
            shortest = length(number)
        if longest < length(number):
            longest = length(number)
        if is_odd(number):
            odds += 1
        if is_prime(number):
            primes += 1
        if is_square(number):
            squares += 1

#determine whether to print digit or digits for shortest and longest
#add the correct string to each variable
    if shortest == 1:
        shortest = str(shortest) + " digit"
    else:
        shortest = str(shortest) + " digits"

    if longest == 1:
        longest = str(longest) + " digit"
    else:
        longest = str(longest) + " digits"

#calculate the average of the numbers
    average = total_sum / total_numbers

#if length of largest number is larger than 10,
# determine right column by that length
    if length(largest) > 10:
        format_string = ">" + str(length(largest) + 3)
        format_string_average = str(format_string) + ".2f"
        
#if length of largest number is smaller than 10,
#use width of 10 for right column to allow room for longest and shortest strings
    else:
        format_string = ">10"
        format_string_average = str(format_string) + ".2f"

#print results, with formating specified to create 2 columns    
    print()
    print("You entered " + str(total_numbers) + " numbers.")
    print(format("Largest: ", "<15") + format(largest, format_string))
    print(format("Smallest: ", "<15") + format(smallest, format_string))
    print(format("Average: ", "<15") + format(average, format_string_average))
    print(format("Shortest: ", "<15") + format(shortest,format_string))
    print(format("Longest: ", "<15") + format(longest,format_string))
    print(format("Num. Odd: ", "<15") + format(odds, format_string))
    print(format("Num. Primes: ", "<15") + format(primes, format_string))
    print(format("Num. Squares: ", "<15") + format(squares, format_string))

#call main function
main()
