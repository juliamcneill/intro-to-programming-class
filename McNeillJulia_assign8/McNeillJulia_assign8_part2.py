"""
McNeillJulia_assign8_part2

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 19 November, 2019
"""

#starting product names, costs, and quantities are put into lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.20, 1.49]
product_quantities = [10, 5, 20]

# search_product
# Input: none
# Processing: Prompts user for a product name (str), validates that the product
#   exists, and find and prints the cost (float) and quantity (int) of that
#   product
# Output: none
def search_product():
    product_name = input("Enter a product name: ")
    #if product name does exist, search for product
    if product_name in product_names:
        #find index of product in lists
        product_index = product_names.index(product_name)
        #find cost of product at index
        cost = product_costs[product_index]
        #find quantity of product at index
        quantity = product_quantities[product_index]
        print('We sell "' + product_name + '" at', format(cost, '.2f'), "per unit")
        print('We currently have', quantity, 'in stock')
    #if product name doesn't exist, alert user
    else:
        print("Sorry, we don't sell \"" + product_name + '"')

# list_product
# Input: none
# Processing: Prints a list of each product (str), in alphabetical order,
#   with their cost (float) and quantities (int)
# Output: none
def list_product():
    #assign new variable names to lists so that you can reassign them by alphabet
    names_sorted = product_names
    costs_sorted = product_costs
    quantities_sorted = product_quantities
    #sort indices by alphabetical order in names_sorted,
    #and sort other lists by same indices
    names_sorted, costs_sorted, quantities_sorted = (list(t) for t in zip(*sorted(zip(names_sorted, costs_sorted, quantities_sorted))))
    #print a list of items, formatted by column
    print("{0:<26s}{1:<7s}{2:<10s}".format("Product", "Price", "Quantity"))
    for i in range(len(names_sorted)):
        print("{0:<26s}{1:<7.2f}{2:<10d}".format(names_sorted[i], costs_sorted[i], quantities_sorted[i]))

# add_product
# Input: none
# Processing: Allows user to add a product (str) to the list, and prompts user
#   to input the name, cost (float), and quantity (int) of that product
# Output: none
def add_product():
    while True:
        product_name = input("Enter a new product name: ")
        #alert user if item already exists
        if product_name in product_names:
            print("Sorry, we already sell that product. Try again.")
            continue
        else:
            while True:
                cost = float(input("Enter a product cost: "))
                #validate that cost is greater than 0
                if cost <= 0:
                    print("Invalid cost. Try again.")
                    continue
                else:
                    while True:
                        quantity = int(input("How many of these products do we have? "))
                        #validate that quantity is greater than 0
                        if quantity <= 0:
                            print("Invalid quantity. Try again.")
                            continue
                        else:
                            #append new name, cost, and quantity to end of lists
                            product_names.append(product_name)
                            product_costs.append(cost)
                            product_quantities.append(quantity)
                            break
                    break
            break
    print("Product added!")

# remove_product
# Input: none
# Processing: Allows user to remove a product (str) from the list, and notifies
#   user if the product they input does not exist
# Output: none
def remove_product():
    product_name = input("Enter a product name: ")
    if product_name in product_names:
        #find index of product details in lists
        product_index = product_names.index(product_name)
        cost = product_costs[product_index]
        quantity = product_quantities[product_index]
        #remove information from this specific index
        product_names.remove(product_name)
        product_costs.remove(cost)
        product_quantities.remove(quantity) 
        print("Product removed!")
    else:
        #alert user if product doesn't exist
        print("Product doesn't exist. Can't remove.")

# update_product
# Input: none
# Processing: Allows user to update the cost (float) or quantity (int) of any
#   product (str), and notifies user if the product they input does not exist
# Output: none       
def update_product():
    product_name = input("Enter a product name: ")
    if product_name in product_names:
        #give you a choice to update cost or quantity
        update_choice = input('What would you like to update? (c)ost or (q)uantity: ')
        #update cost by reassigning index of
        #product in cost list as new cost
        if update_choice == 'c':
            while True:
                cost = float(input("Enter a product cost: "))
                if cost <= 0:
                    print("Invalid cost. Try again.")
                    continue
                else:
                    product_index = product_names.index(product_name)
                    product_costs[product_index] = cost
                    print('Product cost has been updated')
                    break
        #update quantity by reassigning index of
        #product in quantity list as new quantity
        elif update_choice == 'q':
            while True:
                quantity = int(input("How many of these products do we have? "))
                if quantity <= 0:
                    print("Invalid quantity. Try again.")
                    continue
                else:
                    product_index = product_names.index(product_name)
                    product_quantities[product_index] = quantity
                    print('Product quantity has been updated')
                    break
        else:
            #alert user if their letter option isn't cost or quantity
            print('Invalid option')     
    else:
        #alert user if product doesn't exist
        print("Product doesn't exist. Can't update.")

# report_product
# Input: none
# Processing: Allows user to print a report of most expensive product details, least
#   expensive product details, total value of inventory, and a list of the products
#   sorted from lowest to highest price
# Output: none 
def report_product():
    #assign new variable names to lists so that you can reassign them by alphabet
    names_sorted = product_names
    costs_sorted = product_costs
    quantities_sorted = product_quantities
    #sort indices by alphabetical order in names_sorted,
    #and sort other lists by same indices
    costs_sorted, names_sorted, quantities_sorted = (list(t) for t in zip(*sorted(zip(costs_sorted, names_sorted, quantities_sorted))))

    total_costs = 0
    
    for i in range(len(names_sorted)):
        #call deal function
        new_cost = costs_sorted[i] * quantities_sorted[i]
        #update total value
        total_costs += new_cost

    #print a list of items, formatted by column
    print('{0:<30} {1:>5}'.format('Most expensive product: ', costs_sorted[len(names_sorted) - 1]), end=' ')
    print('(' + format(names_sorted[len(names_sorted) - 1], '>10') + ')')
    print('{0:<30} {1:>5}'.format('Least expensive product: ', costs_sorted[0]), end=' ')
    print('(' + format(names_sorted[0], '>10') + ')')
    print('{0:<30} {1:>5.2f}'.format('Total value of inventory: ', total_costs))

    print()

    print('Sorted from lowest price to highest:')
    print("{0:<26s}{1:<7s}{2:<10s}".format("Product", "Price", "Quantity"))
    for i in range(len(names_sorted)):
        print("{0:<26s}{1:<7.2f}{2:<10d}".format(names_sorted[i], costs_sorted[i], quantities_sorted[i]))


#main code of program that repeatedly prompts user to choice an option until
#user quits the program by entering 'q'      
while True:
    print()
    choice = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    if choice.lower() == 's':
        search_product()
    elif choice.lower() == 'l':
        list_product()
    elif choice.lower() == 'a':
        add_product()
    elif choice.lower() == 'r':
        remove_product()
    elif choice.lower() == 'u':
        update_product()
    elif choice.lower() == 'e':
        report_product()
    elif choice.lower() == 'q':
        print("See you soon!")
        break
    else:
        print("Invalid option, try again")
