# Mauricio Corado 1254732

import csv

ManList = input('Enter the Manufacturer file name: ')
PrzList = input('Enter the Price list file name: ')
ServDate = input('Enter the service date list file name: ')

# Reads in the three input files that the user typed in.
with open(ManList) as File:
    read = csv.reader(File)
    ManList = []
    for row in read:
        ManList.append(row)

with open(PrzList) as File:
    read = csv.reader(File)
    price_list = []
    for row in read:
        price_list.append(row)

with open(ServDate) as File:
    read = csv.reader(File)
    service_list = []
    for row in read:
        service_list.append(row)

# sorts all three nested list by their ID so that all fields are aligned
ManList.sort(key=lambda x: x[0])
price_list.sort(key=lambda x: x[0])
service_list.sort(key=lambda x: x[0])

# Sets the item type to laptop which is the type of report we want
item_type = 'tower'
# list of the items to be stored in
tower_list = []
count = 0
# This loop goes through Manufacturer List and populates tower_list only when the item type matches
while count < len(ManList):
    if item_type == ManList[count][2]:
        tower_list.append(ManList[count][0])
        tower_list.append(ManList[count][1])
        tower_list.append(price_list[count][1])
        tower_list.append(service_list[count][1])
        tower_list.append(ManList[count][3])
        count = count + 1
    else:
        count = count + 1


# second loop that makes a list of lists so it can be sorted
final_tower_list = []
count2 = 0
fields = 5
while count2 < len(tower_list):
    final_tower_list.append(tower_list[count2:fields])
    count2 = count2 + 5
    fields = fields + 5

# Sorted the nested list
final_tower_list.sort(key=lambda x: x[0])
print(final_tower_list)
# method to write csv
with open('TowerInventory.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(final_tower_list)
