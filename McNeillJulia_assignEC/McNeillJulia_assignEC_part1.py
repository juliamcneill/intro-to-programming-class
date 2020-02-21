"""
McNeillJulia_assignEC_part1

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 6 December, 2019
""" 
# is_float
# Input:  a string that may represent a floating-point number
# Processing:  check if the string could be converted to a float value
#         without error, by analyzing the characters in the string.
# Output: (bool) True if the string represents a valid float, else False
def is_float(givenstring):
    #set boolean value to false
    float_number = False

    #if the string starts with a -, remove it
    if "-" in givenstring[0:1]:
        givenstring = givenstring[1:]

    #remove one . from the string, if it has one
    #after removing the starting - and one ., check if the string is a digit
    if givenstring.replace(".", "", 1).isdigit():
        float_number = True

    #return the boolean value
    return float_number

#first while loop runs until user gives first valid number
while True:    
    givenstring = input('Enter a floating-point number: ')
    if is_float(givenstring) == True:
        number1 = float(givenstring)
        print('Great.')
        break
    else:
        print('That isn\'t a number.')

#second while loop runs until user gives second valid number
while True:    
    givenstring = input('Enter another floating-point number: ')
    if is_float(givenstring) == True:
        number2 = float(givenstring)
        print('Great.')
        break
    else:
        print('That isn\'t a number.')

#multiply both numbers
result = number1 * number2

print()

#print results
print(number1, '*', number2, '=', result)
    

