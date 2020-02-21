"""
McNeillJulia_assign4_problem3_part3

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 6 October, 2019 
"""
import random

#prompt user to enter the number of sticks they want to start with
number_of_sticks = int(input('How many sticks (10-100)? '))

#ensure that number of sticks is between 10 and 100, and reprompt user if necessary
while number_of_sticks < 10 or number_of_sticks > 100:
    if number_of_sticks < 10:
        print("Sorry, that's too few sticks. Try again.")
    elif number_of_sticks > 100:
        print("Sorry, that's too many sticks. Try again.")
    number_of_sticks = int(input('How many sticks (10-100)? '))

print()

#have user choose the game type: person or computer
game_type = input('Are you playing against a person, or the computer? ').lower()

print()

print("Great. Let's play ...")

print()

#set player tracker to 1
player_turn = 1

#version of game against computer
if game_type == 'computer' or game_type == 'the computer':
    #loop reiterates until number of sticks is 0
    while number_of_sticks > 0:
        #if it is the user's turn:
        if player_turn == 1:
            #print that it is the user's turn it is
            print('Turn: Player 1')
            #print current number of sticks
            print('There are ' + str(number_of_sticks) + ' sticks on the table.')
            #prompt user to take away sticks
            taken_sticks = int(input('How many sticks do you want to take (1, 2 or 3)? '))
            #ensure number entered is 1, 2, or 3, and reprompt user if necessary
            while taken_sticks not in {1, 2, 3}:
                print("Sorry, that's not a valid number.")
                print()
                print('Turn: Player 1')
                print('There are ' + str(number_of_sticks) + ' sticks on the table.')
                taken_sticks = int(input('How many sticks do you want to take (1, 2 or 3)? '))
            #ensure there are enough sticks on the table, and reprompt user if necessary
            while taken_sticks > number_of_sticks:
                print("Sorry, there are not enough sticks on the table.")
                print()
                print('Turn: Player 1')
                print('There are ' + str(number_of_sticks) + ' sticks on the table.')
                taken_sticks = int(input('How many sticks do you want to take (1, 2 or 3)? '))
            #update number of sticks
            number_of_sticks = number_of_sticks - taken_sticks
        #if it is the computer's turn:
        if player_turn == 2:
            #print that it is the computer's turn it is
            print('Turn: Computer')
            #print current number of sticks
            print('There are ' + str(number_of_sticks) + ' sticks on the table.')
            #generate random number of sticks for the computer to take
            taken_sticks = random.randint(1, 3)
            #account for language
            if taken_sticks == 1:
                print('I take ' + str(taken_sticks) + ' stick.')
            else:
                print('I take ' + str(taken_sticks) + ' sticks.')
            #update number of sticks
            number_of_sticks = number_of_sticks - taken_sticks
        #switch players
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1
        print()
    #announce when there are no sticks left
    print('There are no sticks left on the table! Game over.')
    
    #announce winner, based on what player's turn it is
    if player_turn == 1:
        print('Player ' + str(player_turn) + ' wins!')
    else:
        print('Computer wins!')

#version of game against person
elif game_type == 'person' or 'a person':
    #loop reiterates until number of sticks is 0
    while number_of_sticks > 0:
        #print which player's turn it is
        print('Turn: Player ' + str(player_turn))
        #print current number of sticks
        print('There are ' + str(number_of_sticks) + ' sticks on the table.')
        #prompt user to take away sticks
        taken_sticks = int(input('How many sticks do you want to take (1, 2 or 3)? '))
        #ensure number entered is 1, 2, or 3, and reprompt user if necessary
        while taken_sticks not in {1, 2, 3}:
            print("Sorry, that's not a valid number.")
            print()
            print('Turn: Player ' + str(player_turn))
            print('There are ' + str(number_of_sticks) + ' sticks on the table.')
            taken_sticks = int(input('How many sticks do you want to take (1, 2 or 3)? '))
        #ensure there are enough sticks on the table, and reprompt user if necessary
        while taken_sticks > number_of_sticks:
            print("Sorry, there are not enough sticks on the table.")
            print()
            print('Turn: Player ' + str(player_turn))
            print('There are ' + str(number_of_sticks) + ' sticks on the table.')
            taken_sticks = int(input('How many sticks do you want to take (1, 2 or 3)? '))
        #update number of sticks
        number_of_sticks = number_of_sticks - taken_sticks
        #switch players
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1
        print()

    #announce when there are no sticks left    
    print('There are no sticks left on the table! Game over.')
    #announce winner, based on what player's turn it is
    print('Player ' + str(player_turn) + ' wins!')








    




