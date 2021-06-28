# Mauricio Corado 1254732

word_list = [str(i) for i in input().split()]         # gets user input in string format and stores it as a list

count = 0                                   # count is used in order to know when to exit loop

# basic loop that iterates through list and prints deliverable as needed

while count < len(word_list):
    print('{} {}'.format(word_list[count], word_list.count(word_list[count])))
    count = count + 1
