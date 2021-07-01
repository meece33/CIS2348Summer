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

# creates a new list
full_inv = []
count = 0
# Loop that takes in the values in the correct order
while count < len(ManList):
    full_inv.append(ManList[count][0])
    full_inv.append(ManList[count][1])
    full_inv.append(ManList[count][2])
    full_inv.append(price_list[count][1])
    full_inv.append(service_list[count][1])
    full_inv.append(ManList[count][3])
    count = count + 1

# had to create a new list so I can Nest the first list into so it is easier to sort
new_full_inv = []
count2 = 0
fields = 6
while count2 < len(full_inv):
    new_full_inv.append(full_inv[count2:fields])
    count2 = count2 + 6
    fields = fields + 6

# sorts the new nested list
new_full_inv.sort(key=lambda x: x[1])

with open('FullInventory.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new_full_inv)
