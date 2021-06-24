# Mauricio Corado 1254732

import csv                      # import csv as needed
file_name = input()
file = open(file_name, 'r')
read = csv.reader(file)             # reads file into read variable

for line in read:                       # for loop so that it goes through the list
    word_list = line   # original word list with duplicates
    no_dupl = list(dict.fromkeys(word_list))    # crates a new list with no duplicates from the original list

    for i in range(len(no_dupl)):
        print(no_dupl[i], word_list.count(no_dupl[i]))
# for loop iterates over the no duplicate list and prints the word count from word list which is the original