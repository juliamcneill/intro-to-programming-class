"""
McNeillJulia_assign5_problem1

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 22 October, 2019
"""
#prompt user to enter number of herds
while True:
    number_of_herds = int(input('How many herds do you manage? '))
#validate that number of herds is positive
    if number_of_herds > 0:
        break
    print('Invalid input.')

print()

#set number of overall number of rhinos and rhino ages to total
number_of_rhinos_overall = 0
rhino_ages_overall = 0

#set starting values for oldest and youngest rhinos
oldest_rhino = ''
youngest_rhino = ''
oldest_rhino_age = 0
youngest_rhino_age = 1000

#start at the first herd
herd_counter = 1

#use a for loop, set to the input number of herds, to iterate through each herd
for i in range(number_of_herds):
#prompt user to enter number of rhinos in each herd
    while True:
        number_of_rhinos = int(input('How many rhinos in herd #' + str(herd_counter) + '? '))
#validate that number of rhinos is positive
        if number_of_rhinos > 0:
            break
#print response if number of rhinos is 0
        if number_of_rhinos == 0:
            print('There are no rhinos in herd #' + str(herd_counter) + ' so the average age is 0.')
            break
        print("That's impossible.")
        
#set starting values for rhinos within each herd
    rhino_counter = 1
    rhino_names_total = ''
    rhino_ages_total = 0

#use another for loop, set to the input number of rhinos, to iterate through each rhino
    for i in range(number_of_rhinos):
#prompt user to enter each rhino name
        rhino_name = input('Enter the name of rhinoceros #' + str(rhino_counter) + ': ')
#prompt user to enter each rhino age
        while True:
            rhino_age = float(input('How old is ' + str(rhino_name) + '? '))
#validate that each rhino age is over 0
            if rhino_age > 0:
                break
            print("That's impossible.")
#update oldest rhino's info
        if rhino_age > oldest_rhino_age:
            oldest_rhino_age = rhino_age
            oldest_rhino = rhino_name
#update youngest rhino's info
        elif rhino_age < youngest_rhino_age:
            youngest_rhino_age = rhino_age
            youngest_rhino = rhino_name
#update rhino names and ages within each herd
        rhino_names_total += rhino_name
        rhino_ages_total += rhino_age
#break out of loop before adding a comma on the last loop
        if number_of_rhinos == rhino_counter:
            break
#update rhino counter
        rhino_counter += 1
#add comma after each name, besides the last, in rhino name string
        rhino_names_total += ', '
#print out info about herd, providing there is more than 0 rhinos in herd
    if number_of_rhinos != 0:
        print()
        print('The average age for herd #' + str(herd_counter) + ' is ' + str(format(rhino_ages_total/number_of_rhinos, '.2f')))
        print('The rhinos are named: ' + rhino_names_total)
#update overall information, considering all herds
    number_of_rhinos_overall += number_of_rhinos
    rhino_ages_overall += rhino_ages_total
#move to next herd
    herd_counter += 1
    print()

#print out number of rhinos and average age of all rhinos
print('You have ' + str(number_of_rhinos_overall) + ' rhinos all together')
print('The average age is ' + str(format(rhino_ages_overall/number_of_rhinos_overall, '.2f')) + ' years.')

print()

#print out oldest and youngest rhinos
print('The oldest is ' + str(oldest_rhino) + ' at ' + str(oldest_rhino_age) + ' years.')
print('The youngest is ' + str(youngest_rhino) + ' at ' + str(youngest_rhino_age) + ' years.')


