"""
McNeillJulia_assign7_part3

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 7 November, 2019
"""
import random

# generate_code
# Input: length (int)
# Processing: generate a secret code.  The code should have the number of digits specified by length, 
#             using the digits 1 - 9, and without any repeats.
# Return: the secret code (str)
def generate_code(length):
  code = ''.join(random.sample("123456789", length))
  return code

# digits_in_code
# Input: guess (str), code (str)
# Processing: count each digit in guess that also appears in the code
# Return: the count (int)
def digits_in_code(guess, code):
  count = 0
  for i in guess:
    if i in code:
      count += 1

  return count
  
# digits_in_place
# Input: guess (str), code (str)
# Processing: count each digit that appears in the same place in both guess and code
# Return: the count (int)
def digits_in_place(guess, code):
  count = 0
  place_count = 0
  for i in range(len(guess)):
    if guess[i] == code[i]:
      count += 1

  return count

def main():
  #use a while loop to prompt user for length of code and ensure length is valid
  while True:
    length = int(input('How long should the secret code be? '))
    if length > 2 and length < 8:
      break
    print('Code must be between 2 and 8 digits long.')

  #call generate_code function to generate a code of specified length              
  code = generate_code(length)

  #set count of turns equal to 0
  turn_count = 0
  
  #use a while loop to prompt user for each guess, until guess equals code
  while True:
    guess = str(input('What is your guess? '))
    #add 1 to turn count for each guess
    turn_count += 1
    #inform user and restart loop if guess is incorrect number of digits
    if len(guess) != length:
      print('Guess must be', length,'digits long.')
      continue
    #inform user and exit loop if guess equals code
    if guess == code:
      print('You guessed it in', turn_count, 'turns!')
      break
    #call digits_in_code and digits_in_place functions to print information about guess
    print(digits_in_code(guess, code), 'digits are in the code, and', digits_in_place(guess, code), 'are in the correct place.')
    
main()
      
  


