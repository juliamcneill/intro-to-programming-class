"""
McNeillJulia_assign7_part1b

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 7 November, 2019
"""
import string
import random

# function:   password_check
# input:      username (string) and password (string)
# processing: changes invalid password to valid password
# output:     password (string)
def password_fixer(username, password):

    #create strings for each relevant set of characters
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = '#$%&'
    valid_chars = uppercase_letters + lowercase_letters + digits + special_chars

    #remove invalid characters
    original_password = password
    temp_password = ''
    for i in password:
        if i in special_chars or i.isupper() or i.islower() or i.isdigit():
            temp_password += i
            password = temp_password
    if password != original_password:
        print('* New password with invalid characters removed:', password)

    #insert character into username if username is in password
    if username in password:
        username_location = password.find(username)
        char_position = random.randint(username_location, username_location + len(username) - 1)
        char = random.randint(0, len(valid_chars) - 1)
        temp_password = password[0 : char_position] + valid_chars[char] + password[char_position :] 
        password = temp_password
        print('* Username is in password - inserting random character to remove it:', password)

    #insert uppercase character into username if needed
    uppercase_count = 0
    for i in password:
        if i.isupper():
            uppercase_count += 1
    if uppercase_count == 0:
        char_position = random.randint(0, len(password) - 1)
        char = random.randint(0, len(uppercase_letters) - 1)
        temp_password = password[0 : char_position] + uppercase_letters[char] + password[char_position :] 
        password = temp_password
        print('* Adding a random uppercase character at a random position:', password)

    #insert lowercase character into username if needed
    lowercase_count = 0
    for i in password:
        if i.islower():
            lowercase_count += 1
    if lowercase_count == 0:
        char_position = random.randint(0, len(password) - 1)
        char = random.randint(0, len(lowercase_letters) - 1)
        temp_password = password[0 : char_position] + lowercase_letters[char] + password[char_position :] 
        password = temp_password
        print('* Adding a random lowercase character at a random position:', password)

    #insert digit into username if needed
    digit_count = 0
    for i in password:
        if i.isdigit():
            digit_count += 1
    if digit_count == 0:
        char_position = random.randint(0, len(password) - 1)
        char = random.randint(0, len(digits) - 1)
        temp_password = password[0 : char_position] + digits[char] + password[char_position :] 
        password = temp_password
        print('* Adding a random digit character at a random position:', password)

    #insert special character into username if needed
    special_chars = ['#', '$', '%', '&'] 
    special_char_count = 0
    for i in password:
        if i in special_chars:
            special_char_count += 1
    if special_char_count == 0:
        char_position = random.randint(0, len(password) - 1)
        char = random.randint(0, len(special_chars) - 1)
        temp_password = password[0 : char_position] + special_chars[char] + password[char_position :] 
        password = temp_password
        print('* Adding a random special character at a random position:', password)

    #insert extra characters to reach length of 9 if needed
    if len(password) < 9:
        while len(password) < 9:
            char_position = random.randint(0, len(password) - 1)
            char = random.randint(0, len(valid_chars) - 1)
            temp_password = password[0 : char_position] + valid_chars[char] + password[char_position :] 
            password = temp_password
        print('* Adding a random letter to meet the minimum length:', password)

    return password

# function:   password_check
# input:      a username (string) and a password (string)
# processing: prints password results and check if password is valid
# output:     none
def password_check(username, password): 

    #assumes password is valid at start
    valid = True

    #check length of password
    if len(password) < 9: 
        valid = False
    print('* Length of password:', len(password))

    #check if username is in password
    username_in_password = False    
    if username in password:
        username_in_password = True
        valid = False
    print('* Username is part of password:', username_in_password)

    #check that password contains an uppercase character  
    uppercase_count = 0
    for i in password:
        if i.isupper():
            uppercase_count += 1
    if uppercase_count == 0:
        valid = False
    print('* # of uppercase characters in the password:', uppercase_count)

    #check that password contains a lowercase character 
    lowercase_count = 0
    for i in password:
        if i.islower():
            lowercase_count += 1
    if lowercase_count == 0:
        valid = False
    print('* # of lowercase characters in the password:', lowercase_count)

    #check that password contains a digit
    digit_count = 0
    for i in password:
        if i.isdigit():
            digit_count += 1
    if digit_count == 0:
        valid = False
    print('* # of digits in the password:', digit_count)

    #check that password contains a special character
    special_chars = ['#', '$', '%', '&']      
    special_char_count = 0
    for i in password:
        if i in special_chars:
            special_char_count += 1
    if special_char_count == 0:
        valid = False
    print('* # of special characters in the password:', special_char_count)

    #check that password doesn't contain invalid characters
    for i in password:
        if i not in special_chars or i.isupper() or i.islower() or i.isdigit():
            valid = False

    #print whether password is valid or invalid
    if valid: 
        print('Password is valid!') 
    else: 
        print('Password is invalid')
        print()
        #offer user option to have computer fix password
        fix_decision = input('Would you like us to fix your password for you? ')
        if fix_decision.lower() == 'yes':
            password = password_fixer(username, password)
            #print new program-generated password
            print('Your new password is', password)
        else:
            #reprompt user for password if they choose to fix themselves
            password = input('Enter a password: ')
            password_check(username, password)
            print()
  
# function:   password_check
# input:      none
# processing: prompts user for username
# output:     none
def username_input():

    username = input('Enter your username: ')
    print()

    password_input(username)

# function:   password_check
# input:      none
# processing: prompts user for password
# output:     none
def password_input(username):

    password = input('Enter a password: ')

    password_check(username, password)

#call first function         
username_input()
