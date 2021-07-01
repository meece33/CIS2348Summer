# Mauricio Corado 1254732
from datetime import date
from datetime import datetime as dt
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

# Creates a current date and formats it so it can be compared
today = date.today()
TodayFormatted = today.strftime("%m/%d/%Y")
CurrentDate = dt.strptime(TodayFormatted, "%m/%d/%Y")

# list of the items to be stored in
PSD_list = []
count = 0
# This loop goes through Manufacturer List and populates PSD_list only when service date is < current date
while count < len(ManList):
    a = dt.strptime(service_list[count][1], "%m/%d/%Y")         # converts to a time instead of string
    if a < CurrentDate:
        PSD_list.append(ManList[count][0])
        PSD_list.append(ManList[count][1])
        PSD_list.append(ManList[count][2])
        PSD_list.append(price_list[count][1])
        PSD_list.append(service_list[count][1])
        PSD_list.append(ManList[count][3])
        count = count + 1
    else:
        count = count + 1
print(PSD_list)

# second loop that makes a list of lists so it can be sorted
final_PSD_list = []
count2 = 0
fields = 6
while count2 < len(PSD_list):
    final_PSD_list.append(PSD_list[count2:fields])
    count2 = count2 + 6
    fields = fields + 6

# Sorted the nested list
final_PSD_list.sort(key=lambda x: x[4])
print(final_PSD_list)
# method to write csv
with open('PastServDate.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(final_PSD_list)
