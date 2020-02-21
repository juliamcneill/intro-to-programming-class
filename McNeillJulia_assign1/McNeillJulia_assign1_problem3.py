"""
McNeillJulia_assign1_problem3

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 15 September, 2019 
"""

# This requests three test scores from the user, one at a time.
test_score1 = int(input('Enter the score for student #1: '))
test_score2 = int(input('Enter the score for student #2: '))
test_score3 = int(input('Enter the score for student #3: '))

print('')

# This creates a variable for the name of the class, and then prints a title for the information.
class_name = 'Introduction to Computer Programming'
print('Test Scores For "' + class_name + '":')

# This prints each test score submitted.
print('- Student #1: ' + str(test_score1))
print('- Student #2: ' + str(test_score2))
print('- Student #3: ' + str(test_score3))

#This calculates the average test score by adding all three test scores and dividing the total by 3.
average_score = (test_score1 + test_score2 + test_score3) / 3

#This prints the average test score for the class.
print('Class average: ' +  str(average_score))




