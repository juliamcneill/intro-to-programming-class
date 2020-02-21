"""
McNeillJulia_assign3_problem4

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 29 September, 2019
"""
#request the start date and birth date from the user
print("Enter the show start date and the contestant's birthdate to determine their age at the start of taping.")
start_date = input('Enter start date (MMDDYYYY): ')
birth_date = input('Enter birth date (MMDDYYYY): ')

#extract the relevant section of each string for month, day, and year
start_month = int(start_date[0:2])
start_day = int(start_date[2:4])
start_year = int(start_date[4:8])
birth_month = int(birth_date[0:2])
birth_day = int(birth_date[2:4])
birth_year = int(birth_date[4:8])

#assign a birth month name to each birth month number
if birth_month == 1:
    birth_month_name = 'January'
elif birth_month == 2:
    birth_month_name = 'February'
elif birth_month == 3:
    birth_month_name = 'March'
elif birth_month == 4:
    birth_month_name = 'April'
elif birth_month == 5:
    birth_month_name = 'May'
elif birth_month == 6:
    birth_month_name = 'June'
elif birth_month == 7:
    birth_month_name = 'July'
elif birth_month == 8:
    birth_month_name = 'August'
elif birth_month == 9:
    birth_month_name = 'September'
elif birth_month == 10:
    birth_month_name = 'October'
elif birth_month == 11:
    birth_month_name = 'November'
else:
    birth_month = 'December'

#add the relevant suffix to each birth day number
if 4 <= birth_day <= 20 or 24 <= birth_day <= 30:
    suffix = 'th'
elif birth_day == 1 or birth_day == 21 or birth_day == 31:
    suffix = 'st'
elif birth_day == 2 or birth_day == 22:
    suffix = 'nd'
else:
    suffix = 'rd'

#print out the contestant's date of birth with correct formatting
print('The contestant was born on', birth_month_name, str(birth_day) + suffix + ',', str(birth_year))

#determine if the contestant will be 21 and print result
#older than 21
if birth_year + 21 < start_year:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
#younger than 21
elif birth_year + 20 > start_year:
    print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
#within a year of 21, but more than a month older
elif birth_month < start_month:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
#within a month of 21, but older
elif birth_day <= start_day:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
#within a year of 21, but younger
else:
    print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
