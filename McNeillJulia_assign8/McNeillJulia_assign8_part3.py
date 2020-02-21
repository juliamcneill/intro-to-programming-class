"""
McNeillJulia_assign8_part3

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 19 November, 2019
"""
import random

#create list of cards and list of their respective values
cards = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', 
          '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 
          'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', 
          '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', 
          '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 
          'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', 
          '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', 
          '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 
          'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', 
          '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', 
          '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 
          'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 
          10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 
          4, 3, 2, 1, 10, 10, 10]

# deal
# Input: nothing
# Processing: Randomly choose a card and remove it from the deck
# Output: The name of the card (str) and the point value for the card (int)
def deal():
    #find a random integer for the length of the card deck
    i = random.randint(0, len(cards))

    #find the card and point value at that index
    card = cards[i]
    point_value = values[i]

    #remove this card and point_value from the lists
    cards.remove(card)
    values.remove(point_value)

    '''
    #check that deal function works
    print('deal function:')
    print(card)
    print(point_value)
    print()
    '''

    #return the card and point_value that you have removed
    return card, point_value

# init_hand
# Input: nothing
# Processing: Deal two cards into the player's hand, by calling the deal function twice
# Output: three values: a list for the card names dealt, a list for the values of those 
#        cards, and an int which is the total point value of the cards just dealt (int)
def init_hand():
    #create empty lists for the names and point values of the two cards to be dealt
    hand_card_names = []
    hand_point_values = []
    #set the total value of the cards equal to 0
    total_values = 0

    #deal two cards
    for x in range(0, 2):
        #call deal function
        new_card_name, new_point_value = deal()

        #append new cards to hand lists
        hand_card_names.append(new_card_name)
        hand_point_values.append(new_point_value)

        #update total value
        total_values += new_point_value

    '''
    #check that init_hand function works
    print('init_hand function:')
    print(hand_card_names)
    print(hand_point_values)
    print(total_values)
    print()
    '''

    #return two lists and total value integer
    return hand_card_names, hand_point_values, total_values

# reset_deck
# Input: List of the cards in the hand, and parallel list of the card values
# Processing: Puts the hands (and values) back in the deck (add them to the
#       main lists of cards and values)
# Output: Nothing
def reset_deck(hand_card_names, hand_point_values):

    #return two cards to deck
    for i in range(0, 2):

        #find cards to append from init_hand function
        appended_card = hand_card_names[i]
        appended_value = hand_point_values[i]

        #append cards to end of original lists
        cards.append(appended_card)
        values.append(appended_value)

        '''
        #check that reset_deck function works
        print(cards)
        print(values)
        '''

'''
#check that each function works
deal()
print('break')
init_hand()
reset_deck()
hand_card_names, hand_point_values, total_values = init_hand()
reset_deck(hand_card_names, hand_point_values)
'''



















    
