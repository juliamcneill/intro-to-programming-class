"""
McNeillJulia_assign9

Written by: Julia McNeill
Written for: Intro to Programming section 4, Mo-Wed 9:30am, Fall 2019

Date: 3 December, 2019
"""
#generate list from string of exam answers
answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answers_stripped = answerkey.split(",")

# read_file
# Input: none
# Processing: Prompt user until they give a valid file name and then open file
# Output: none
def read_file():
    #prompt user for file name
    filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")
    try:
        #open file
        file = open(filename + ".txt")
        print("Successfully opened", filename + ".txt")
        #call analyse_file function
        analyse_file(filename, file)
    except IOError:
        print("File cannot be found.")
        print()
        #reprompt user until they give a filename that does not generate an error
        read_file()

# analyse_file
# Input: filename (str) and file contents
# Processing: Count and print all invalid lines, append the scores of valid lines onto
#   a list, calculate mean, highest, lowest, range, median, and mode of all
#   valid scores, and print results
# Output: none
def analyse_file(filename, file):
    print()
    print("**** ANALYZING ****")
    print()
    #keep track of number of valid and invalid lines
    valid_lines = 0
    invalid_lines = 0
    #keep track of N numbers and scores from each line in lists
    N_numbers_list = []
    score_list = []
    #iterate through each line/student
    for line in file.readlines():
        #split line by commas
        line_stripped = line.strip().split(",")
        #ensure that line has 26 values
        if len(line_stripped) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(line)
            invalid_lines += 1
        else:
            valid = True
            #ensure that N number is in proper format
            if line_stripped[0][0] != 'N' or len(line_stripped[0]) != 9:
                valid = False
            else:
                for c in range(1, len(line_stripped[0])):
                    if not line_stripped[0][c].isdigit():
                        valid = False
                        break
            if valid == False:
                invalid_lines +=1
                print("Invalid line of data: N# is invalid")
                print(line)
            #if line is valid, update student score and add information to
            #N number and score lists
            else:
                valid_lines += 1
                score = 0
                for i in range(1, len(line_stripped)):
                    if line_stripped[i] == answers_stripped[i-1]:
                        score += 4
                    elif line_stripped[i] != '':
                        score += -1
                score_list.append(score)
                N_numbers_list.append(line_stripped[0])        
    if invalid_lines == 0:
        print("No errors found!")

    #calculate mean score
    mean_score = sum(score_list) / len(score_list)
    #calculate highest score
    highest_score = max(score_list)
    #calculate lowest score
    lowest_score = min(score_list)
    #calculate range of scores
    score_range = highest_score - lowest_score
    
    #calculate median score
    median = 0
    temp_list = score_list.copy()
    temp_list.sort()
    if (len(score_list) % 2) != 0:
        median_score = (temp_list[len(temp_list) // 2] + temp_list[(len(temp_list) - 1) // 2]) / 2
    else:
        median_score = temp_list[len(temp_list) // 2]

    #calculate mode score(s)
    count_dictionary = {}
    count_list = []
    for i in score_list:
        count_i = score_list.count(i)
        count_list.append(count_i)
        count_dictionary[i] = count_i
    max_count = max(count_list)
    if max_count == 1:
        mode_score = "None"
    else:
        mode_score = []
        for key, item in list(count_dictionary.items()):
            if item == max_count: 
                mode_score.append(str(key))
        mode_score.sort()

    #print report on student scores
    print()
    print("**** REPORT ****")
    print()
    print("Total valid lines of data:", valid_lines)
    print("Total invalid lines of data:", invalid_lines)
    print()
    print("Mean (average) score:", format(mean_score, ".2f"))
    print("Highest score:", highest_score)
    print("Lowest score:", lowest_score)
    print("Range of scores:", score_range)
    print("Median score:", format(median_score, ".1f"))
    print("Mode score(s):", ' '.join(mode_score))
    #calculate generate_file function
    generate_file(filename, score_list, N_numbers_list, mean_score)

# analyse_file
# Input: filename (str), list of scores (list), list of N numbers (list), mean score (float)
# Processing: Ask user if they would like to apply a curve to the scores, and generate
#   a new file with scores for each student listed
# Output: none
def generate_file(filename, score_list, N_numbers_list, mean_score):
    while True:
        #prompt user to choose whether they curve their scores
        curve_decision = input("Would you like to apply a curve to the scores? (y)es or (n)o? ")
        #if curve decision is no, write file with N numbers and grades 
        if curve_decision.lower() == "n":
            generated_file = filename + "_grades.txt"
            out = open(generated_file, "w")
            i = 0
            while i < len(N_numbers_list):
                out.write('{:s},{:d}\n'.format(N_numbers_list[i],score_list[i]))
                i += 1
            break
        #if curve decision is yes, write file with N numbers, grades, and new
        #curved grades that add the difference between the desired mean and the actual mean
        #to each student's grade
        elif curve_decision.lower() == "y":
            desired_mean = float(input("Enter desired mean score: "))
            curve_amount = desired_mean - mean_score
            generated_file = filename + "_grades_with_curve.txt"
            out = open(generated_file, "w")
            i = 0
            while i < len(N_numbers_list):
                curved_score = float(score_list[i]) + curve_amount
                out.write('{:s},{:d},{:s}\n'.format(N_numbers_list[i], score_list[i], format(curved_score, ".2f")))
                i += 1
            break
    print("Done! A new grade file has been written (" + generated_file + ")")
    out.close()
    
read_file()
