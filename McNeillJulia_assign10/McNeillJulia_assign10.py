"""
McNeillJulia_assign10

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 10 December, 2019
"""
import time
import string

#start time
start_time = time.time()

#create 'words' dictionary
words = {}

#download review data from file
file_object = open('movie_reviews.txt', 'r')
data_raw = file_object.read()
file_object.close()

#format the data by making lowercase and splitting by line
data_lowercase = str.lower(data_raw)
data_split = data_lowercase.split('\n')

#keep track of line count
line_count = 0

#this block analyzes sentiment for each word in the data
print('Initializing sentiment database.')
#for each line of data
for review in data_split:
    #split by word
    data_final = review.split(' ')
    #ensure that first character of line is an integer
    #and skip over line if it is not
    if data_final[0].isdigit() == False:
        continue
    #count each valid line
    line_count += 1
    #for each word in the line
    for word in data_final:   
        #add new word to dictionary of words, using a list
        #first index is count of how many times the word appears
        #second index is total sum of sentiment (first character)
        #of line word appears in
        if word not in words:
            words[word] = [1, int(data_final[0])]
        #update existing word by updating each index of list
        else:
            words[word][0] += 1
            words[word][1] += int(data_final[0])

#end time
end_time = time.time()
time = end_time - start_time

#print results of database analysis
print('Sentiment database initialization complete.')
print('Read', line_count ,'lines.')
print('Total unique words analyzed:', len(words))
print('Analysis took', format(time, '.3f'), 'seconds to complete.')
print('')

#loop until user prompts to quit program
while True:
    #prompt for phrase to test
    phrase = input('Enter a phrase to test: ')

    #if user decides to quit, end loop
    if phrase == 'quit':
        print('Quitting.')
        break

    #clean up phrase: make lowercase, remove punctuation, split by word
    phrase_lowercase = str.lower(phrase)
    punctuation = "".join(c for c in string.punctuation if c not in ("'","-"))
    phrase_without_punctuation = "".join(c for c in phrase_lowercase if c not in punctuation)
    phrase_split = phrase_without_punctuation.split()

    #keep track of total score for phrase
    average_total = 0
    #keep track of number of scores for phrase
    scores_total = 0

    #for each word in phrase
    for word in phrase_split:
        #if word is in dictionary of words
        if word in words:
            #calculate average sentiment for word
            average_score = words[word][1] / words[word][0]
            #print word, number of times it occurs, and average sentimental
            print("* '", word, "' appears ", words[word][0], ' times with an average score of ', average_score, sep = '')
            average_total += average_score
            scores_total += 1
        #if word is not in dictionary of words
        else:
            print("* '", word, "' does not appear in any movie reviews.", sep = '')
    #if no words in phrase appear in dictionary
    if scores_total == 0:
        print('Not enough words to determine sentiment.')
    #print average sentimental for phrase
    else:
        print('Average score for this phrase is:', average_total / scores_total)
        #print if phrase is positive or negative
        if (average_total / scores_total) > 2:
            print('This is a POSITIVE phrase.')
        else:
            print('This is a NEGATIVE phrase.')
    print()

    
