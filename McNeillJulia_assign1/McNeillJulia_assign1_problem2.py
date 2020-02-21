"""
McNeillJulia_assign1_problem2

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 15 September, 2019 
"""

#This requests three names from the user, one at a time.
name1 = input('Please enter name #1: ')
name2 = input('Please enter name #2: ')
name3 = input('Please enter name #3: ')

print('')

#This prints a statement that tells the user what the program is generating.
print('Here are your names in every possible order:')
print('--------------------------------------------')

#The following lines print the three names in various orders, with various formatting.

print('')

print('1. ' + name1 + ', ' + name2 + ', ' + name3)

print('')

print('2. *' + name1 + '* *' + name3 + '* *' + name2)

print('')

print('3. ' + name2 + '-' + name1 + '-' + name3)

print('')

print('4. ' + name2 + '\n' + name3 + '\n' + name1)

print('')

print('5. ' + name3 + '\n   ' + name2 + '\n   ' + name1)

print('')

print('6. ' + name3 + '\n---' + name1 + '\n---' + name2)




