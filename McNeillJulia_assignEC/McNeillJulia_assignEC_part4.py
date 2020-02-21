"""
McNeillJulia_assignEC_part4

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 6 December, 2019
"""
# function:    listlen
# INPUT:       a list
# PROCESSING:  determines the size of the list
# OUTPUT:      an integer representing the size of the list
def listlen(mylist):
    list_size = 0

    #use tracker on for loop to find list size
    for i in mylist:
        list_size += 1
        
    return list_size

# function:    listmax
# INPUT:       a list
# PROCESSING:  obtains the largest element in the list
# OUTPUT:      returns the largest element in the list
def listmax(mylist):

    #if mylist is empty, return 'None'
    if not mylist:
        largest_element = 'None'
    else:
        #set default largest element
        largest_element = mylist[0]

        #find largest element using for loop
        for i in mylist:
            if i > largest_element:
                largest_element = i
     
    return largest_element

# function:    listcopy
# INPUT:       a list
# PROCESSING:  creates a new list which serves as a copy of the supplied list
# OUTPUT:      returns a new copy of the list
def listcopy(mylist):

    #create new list that is size of old list and fill with blank values
    list_size = listlen(mylist)
    new_copy = [None] * list_size

    index = 0

    #copy over each value from mylist individually
    for i in mylist:
        new_copy[index] = i
        index += 1

    return new_list

# function:    listappend
# INPUT:       a list and an element to add to the list (any data type)
# PROCESSING:  creates a new list which includes the new element appended
#              to the end of the list
# OUTPUT:      returns a new copy of the list
def listappend(mylist, list_addition):

    #create new list that is one index longer than old list and fill with blank values
    new_list_size = listlen(mylist) + 1
    new_list = [None] * new_list_size

    index = 0

    #copy over each value from mylist individually
    for i in new_list[:new_list_size-1]:
        new_list[index] = mylist[index]
        index += 1

    #add new addition to last index
    new_list[new_list_size - 1] = list_addition

    return new_list

# function:    listinsert
# INPUT:       a list, a location (integer) and a data 
#              element (can be a string, float, Boolean or 
#              int)
# PROCESSING:  inserts the supplied data element into the 
#              list at the desired location
# OUTPUT:      return a new copy of the list that contains
#              the inserted element
def listinsert(mylist, addition_location, list_addition):

    #create new list that is one index longer than old list and fill with blank values
    new_list_size = listlen(mylist) + 1
    new_list = [None] * new_list_size

    index = 0

    for i in new_list:
        #add new addition at given location
        if index == addition_location:
            new_list[index] = list_addition
        #if you have not passed location yet
        elif index < addition_location:
            new_list[index] = mylist[index]
        #if you have passed location, shift index by one
        elif index > addition_location:
            new_list[index] = mylist[index - 1]
        index += 1

    return new_list

# function:    listremove
# INPUT:       a list and a data element (can be a string, 
#              float, Boolean or int)
# PROCESSING:  removes all occurrences of the supplied 
#              data element from the list.  You can assume 
#              that the data element is present in the list 
#              somewhere.
# OUTPUT:      return a new copy of the list with the
#              desired element removed
def listremove(mylist, list_subtraction):

    #create new list that is one index longer than old list and fill with blank values
    new_list_size = listlen(mylist) - 1
    new_list = [None] * new_list_size

    index = 0
    #keep track of whether you have passed subtracting
    passed_subtraction = False

    #copy over values from list to list
    for i in mylist:
        if i == list_subtraction:
            passed_subtraction = True
        elif passed_subtraction == False:
            new_list[index] = i
        #skip over value to subtract
        elif passed_subtraction == True:
            new_list[index - 1] = i
        index += 1

    return new_list

# function:    listreverse
# INPUT:       a list
# PROCESSING:  creates a copy of the supplied list that
#              contains the same elements as the original
#              list, but in reverse order
# OUTPUT:      return a new copy of the list in reverse order
def listreverse(mylist):

    #create new list that is length of mylist
    new_list = [None] * listlen(mylist)

    #track length of copy
    length_copy = listlen(mylist)

    #subtract length by one each time, and use length as index to draw from
    for i in mylist:
        length_copy -= 1
        new_list[length_copy] = i

    return new_list

# function:    append_unique
# INPUT:       a list,  a data element (can be a string, float, Boolean or int)
# PROCESSING:  appends the supplied data element to the 
#              list only if it does not already exist in the list
# OUTPUT:      return a new copy of the list that contains
#              the inserted element
def append_unique(mylist, list_addition):

    new_list = []

    #if number is already in list, return contents of mylist
    if list_addition in mylist:
        new_list = mylist
    else:
        #create new list that is one index longer than old list and fill with blank values
        new_list_size = listlen(mylist) + 1
        new_list = [None] * new_list_size

        index = 0

        #transfer over content of list
        for i in new_list[:new_list_size-1]:
            new_list[index] = mylist[index]
            index += 1

        #add new list value at end
        new_list[new_list_size - 1] = list_addition

    return new_list

# function:    insert_in_order
# INPUT:       a list that is already sorted in ascending order,  
#			   a data element (must be same type as all elements in the given list)
# PROCESSING:  assume the given list is in order, find where the new element belongs in that order, and 
#              insert it into the list in that place
# OUTPUT:      return a new copy of the list that contains
#              the inserted element and is sorted in ascending order

#i did what i could figure out, could not figure out how to account for repeat numbers in
#mylist at the point where you put in the list_addition

def insert_in_order(mylist, list_addition):

    #if list is empty, add list addition as only index and return new list
    if not mylist:
        new_list = [None]
        new_list[0] = list_addition
        return new_list

    #if list is not empty
    #new list size is 1 larger than mylist size
    new_list_size = listlen(mylist) + 1
    #create new list with blank values
    new_list = [None] * new_list_size

    index = 0

    #note first index in mylist that list addition passes value
    for i in mylist:
        if list_addition >= i:
            passing = i
            break

    #insert list addition at point of temp value
    #something is wrong in this part of the code, but i couldn't figure this one out
    for i in new_list:
        if i == passing:
            new_list[index] = list_addition
            new_list[index + i] = mylist[index]
            index += 1
        elif index < passing:
            new_list[index] = mylist[index]
        elif index > passing:
            new_list[index] = mylist[index - 1]
        index += 1

    return new_list
