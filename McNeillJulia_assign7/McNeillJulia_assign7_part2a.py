"""
McNeillJulia_assign7_part2a

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 7 November, 2019
"""
import random
import string

# function:   add_letters
# input:      a word to scramble (String) and a number of letters (integer)
# processing: adds a number of random letters (A-Z; a-z) after each letter 
#             in the supplied word. for example, if word="cat" and num=1 
#             we could generate any of the following:
#             cZaQtR
#             cwaRts
#             cEaett
# 
#             if word="cat" and num=2 we could generate any of the following:
#             cRtaHFtui
#             cnnaNYtjn
#             czAaAitym
#
# output:     returns the newly generated word
def add_letters(word, number):
  #create string with letters
  letters = string.ascii_letters

  new_word = ''

  #use a for loop to insert the letters in the word
  for i in range(len(word)):
    new_word += word[i]
    for i in range(number):
      random_letter = random.choice(letters)
      new_word += random_letter
  
  return new_word

# function:   remove_letters
# input:      a word to unscramble (String) and the number of characters to remove (integer)
# processing: the function starts at the first position in the supplied word and keeps it.
#             it then removes "num" characters from the word. the process is repeated again
#             if the word contains additional characters - the next character is kept
#             and "num" more characters are removed.  For example, if word="cZaYtU" and
#             num=1 the function will generate the following:
#        
#             cat (keeping character 0, removing character 1, keeping character 2, removing
#                  character 3, keeping character 4, removing character 5)
#
# output:     returns the newly unscrambed word
def remove_letters(word, number):
  new_word = ''

  #use a for loop to remove the letters in the word
  for i in range(len(word)):
    if i % (number + 1) == 0:
      new_word += word[i]
       
  return new_word

# function:   shift_characters
# input:      a word (String) and a number of characters to shift (integer)
# processing: shifts each character in the supplied word to another position in the ASCII
#             table. the new position is dictated by the supplied integer.  for example,
#             if word = "apple" and num=1 the newly generated word would be:
#
#             bqqmf
#
#             because we added +1 to each character. if we were to call the function with
#             word = "bqqmf" and num=-1 the newly generated word would be:
#           
#             apple
#
#             because we added -1 to each character, which shifted each character down by
#             one position on the ASCII table.
#
# output:     returns the newly generated word
def shift_characters(word, shift):
   new_word = ''

   #use a for loop to shift the letters in the word
   for i in word:
       new_ord = ord(i) + shift
       new_word += chr(new_ord)
       
   return new_word

'''
#sample program to check add_characters function
original = "Hello!"

for num in range(1, 5):
    scrambled = add_letters(original, num)
    print ("Adding", num, "random characters to", original, "->", scrambled)

print()

#sample program to check remove_characters function
word1 = "HdeulHlHom!t"
word2 = "HTLedklFNljioMH!bi"
word3 = "HHHZeZrflqSflzOiosNU!jBk"
word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"

unscrambled1 = remove_letters(word1, 1)
print ("Removing 1 characer from", word1, "->", unscrambled1)

unscrambled2 = remove_letters(word2, 2)
print ("Removing 2 characers from", word2, "->", unscrambled2)

unscrambled3 = remove_letters(word3, 3)
print ("Removing 3 characers from", word3, "->", unscrambled3)

unscrambled4 = remove_letters(word4, 4)
print ("Removing 4 characers from", word4, "->", unscrambled4)

print()

# sample program to check shift_characters function
word1 = "apple"

newword1 = shift_characters(word1, 1)
print (word1, "shifted by +1 is", newword1)

unscrambled1 = shift_characters(newword1, -1)
print (newword1, "shifted by -1 is", unscrambled1)

word2 = "Pears are yummy!"

newword2 = shift_characters(word2, 2)
print (word2, "shifted by +2 is", newword2)

unscrambled2 = shift_characters(newword2, -2)
print (newword2, "shifted by -2 is", unscrambled2)
'''
    

