# Mauricio Corado 1254732

nums_list = [int(i) for i in input().split()]      # Receives input and stores it in list num_list
no_neg_list = []                                 # initiates a list that will store just the nums that are +

for i in nums_list:     # loop that goes through num_list and adds all positive nums to no_neg_list
    if i >= 0:
        no_neg_list.append(i)

sort_list = sorted(no_neg_list)         # sorts the list that contains the positive nums

count = 0
while count < len(sort_list):                 # loop used to print just the number without list form
    print(sort_list[count], end=' ')
    count = count + 1
