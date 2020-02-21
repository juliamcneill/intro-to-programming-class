"""
McNeillJulia_assign2_problem2

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 22 September, 2019 
"""
#prompt the user to enter two values
value1 = int(input('Enter value 1: '))
value2 = int(input('Enter value 2: '))

print()

#print a title for what the program is calculating
print('Place Value Totals: ')

print()

#divide each value by 10 and return the remainder
#(the remainder for each is the ones digit)
#add the ones digits and displays the sum
print(format("\t%d + %d =", "<11") % (value1%10, value2%10), format("%d ones", ">7") % (value1%10 + value2%10))

#divide each value by 10 and drop the decimal. divide this value by 10 and return the remainder
#(the remainder for each is the tens digit of the original number)
#add the tens digits and displays the sum
print(format("\t%d + %d =", "<11") % ((value1//10)%10, (value2//10)%10), format("%d tens", ">7") % ((value1//10)%10 + (value2//10)%10))

#divide each value by 100 and drop the decimal. divide this value by 10 and return the remainder
#(the remainder for each is the hundreds digit of the original number)
#add the hundreds digits and displays the sum
print(format("\t%d + %d =", "<11") % ((value1//100)%10, (value2//100)%10), format("%d hundreds", ">7") % ((value1//100)%10 + (value2//100)%10))

#divide each value by 1000and drop the decimal. divide this value by 10 and return the remainder
#(the remainder for each is the thousands digit of the original number)
#add the thousands digits and displays the sum
print(format("\t%d + %d =", "<11") % (value1//1000, value2//1000), format("%d thousands", ">7") % (value1//1000 + value2//1000))




