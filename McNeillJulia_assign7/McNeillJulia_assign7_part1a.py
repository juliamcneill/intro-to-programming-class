"""
McNeillJulia_assign7_part1a

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 7 November, 2019
""" 
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
        print('Password is invalid, please try again')
        print()
        #reprompt user for password if invalid
        password_input(username)
  
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
