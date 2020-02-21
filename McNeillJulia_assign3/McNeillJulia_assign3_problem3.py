"""
McNeillJulia_assign3_problem3

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 29 September, 2019
"""
# INPUT
#request three names from the user
name1 = input("Enter a name: ")
name2 = input("Enter a name: ")
name3 = input("Enter a name: ")

print()

# PROCESSING
#set the variable names_in_order to be equal to True
#in the rest of the program, we will change this variable
#to False if the names are not in order
names_in_order = True

#then, sort the names
#first, put first two names in order
#check if they are out of order (name1 > name2), and if so,
#switch them using a temporary variable
#compare all-lowercase, to disregard capitalization 
if str.lower(name1) > str.lower(name2):
    temp = name1
    name1 = name2
    name2 = temp
    names_in_order = False

#then, put name3 in the correct place relative to name1 and name2
#check if name3 is lower than name1 and name2, and if so,
#swap it out for name1
if str.lower(name3) < str.lower(name1):
    temp = name3
    name3 = name2
    name2 = name1
    name1 = temp
    names_in_order = False

#if not, check if name3 is between name1 and name2, and if so,
#swap it with name2
elif str.lower(name1) < str.lower(name3) < str.lower(name2):
    temp = name3
    name3 = name2
    name2 = temp
    names_in_order = False

#if neither, name3 is already in the correct place, as name3

# OUTPUT
#the processing code has put all three names in order,
#so we can just print them out for the user to see
print('Names Sorted:')
print(name1)
print(name2)
print(name3)

print()

#test whether names_in_order was changed to false throughout the process
#display this information
if names_in_order == False:
    print('You entered some names out of order.')
else:
    print('You entered all names in order.')

            

