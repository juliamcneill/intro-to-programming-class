"""
McNeillJulia_assign7_part2b

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 7 November, 2019
"""
#import functions from other document
from McNeillJulia_assign7_part2a import add_letters, remove_letters, shift_characters

#use a while loop to keep prompting user until they quit
while True:
  user_letter = input('(e)ncode, (d)ecode or (q)uit: ')

#if user's letter is q, quit loop and end program
  if user_letter == 'q':
    break;

#if user's letter is e, proceed with encoding
  elif user_letter == 'e':
#prompt for user to input number and phrase
    user_number = int(input('Enter a number between 1 and 5: '))
    user_phrase = input('Enter a phrase to encode: ')
#call add_letters and shift_characters functions
    user_phrase = add_letters(user_phrase, user_number)
    user_phrase = shift_characters(user_phrase, user_number)
#print encoded word and exit loop
    print('Your encoded word is:', user_phrase)
    print()

#if user's letter is d, proceed with decoding
  elif user_letter == 'd':
#prompt for user to input number and phrase
    user_number = int(input('Enter a number between 1 and 5: '))
    user_phrase = input('Enter a phrase to decode: ')
#call remove_letters and shift_characters functions
    user_phrase = remove_letters(user_phrase, user_number)
    user_phrase = shift_characters(user_phrase, -user_number)
#print decoded word and exit loop
    print('Your decoded word is:', user_phrase)
    print()

#if any other letter, let them know that input is invalid and continue loop
  else:
    print('Invalid input.')



  
