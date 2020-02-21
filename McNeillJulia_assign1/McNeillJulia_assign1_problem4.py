"""
McNeillJulia_assign1_problem4

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 15 September, 2019 
"""

# This prompts the user to enter a volume in milliliters.
quantity_in_milliliters = float(input('Enter the volume in milliliters: '))

# This takes the volume in milliliters that was entered and converts it into various different measurement units.
quantity_in_tsp = quantity_in_milliliters * 0.202884
quantity_in_tbsp = quantity_in_tsp / 3
quantity_in_cups = quantity_in_tbsp / 16
quantity_in_pints = quantity_in_cups / 2 
quantity_in_quarts = quantity_in_pints / 2
quantity_in_gallons = quantity_in_quarts / 4
quantity_in_fl_oz = quantity_in_milliliters / 29.5735

# This prints each of the measurement units that was just calculated for the user to see.
print('')
print('--------------------------------------------------------------')
print('		 mL to US Fluid Volume Units		             ')
print('--------------------------------------------------------------')

print('          mL:           ' + str(quantity_in_milliliters))
print('         tsp:           ' + str(quantity_in_tsp))
print('        tbsp:           ' + str(quantity_in_tbsp))
print('      cup(s):           ' + str(quantity_in_cups))
print('     pint(s):           ' + str(quantity_in_pints))
print('    quart(s):           ' + str(quantity_in_quarts))
print('   gallon(s):           ' + str(quantity_in_gallons))
print('       fl oz:           ' + str(quantity_in_fl_oz))

print('--------------------------------------------------------------')
