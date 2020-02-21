"""
McNeillJulia_assign8_part1

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 19 November, 2019
"""
#create a loop to reprompt user for integer until they enter 10 or higher
while True:
    n = int(input("Enter a positive integer greater than or equal to 10: "))
    if n >= 10:
        break
    else:
        print('Invalid number!')
        print()

#set up empty list of primes       
primes = []
#add 'P' (prime) to each list index for the integer user has input
for i in range(0, n + 1):
    primes.append('P')

#switch indices 0 and 1 to 'N' (not prime)
primes[0] = 'N'
primes[1] = 'N'

#this loop labels each non-prime number as 'N' (not prime)
#iternates from 2 to half of n, as going this far will catch all non-prime numbers
for i in range(2, n // 2):
    #checks each number between each number that is 'P' (prime) and n 
    if primes[i] == 'P':
        for j in range(i + 1, n):
            #if the number is a multiple of the prime number, label it as non-prime
            if j % i == 0:
               primes[j] = 'N'
               
#set prime count equal to 0
prime_count = 0

#this loop prints all prime numbers
for i in range(2,n):
    if primes[i] == 'P':
        #prime count increases by one for each prime number
        prime_count += 1
        #sets 10 numbers to each line
        if prime_count % 10 == 0:
            print('{0:>7}'.format(i))
        else:
            print('{0:>7}'.format(i), end='')

#sets the total count line on the next line, after the prime numbers
if not prime_count % 10 == 0:
    print()

#print total count of prime numbers
print('Found', prime_count, 'prime numbers!') 
    
    


