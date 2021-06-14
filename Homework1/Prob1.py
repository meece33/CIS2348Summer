# Mauricio Corado 1254732


print('Birthday Calculator\nCurrent day')
Cmonth = int(input('Month:'))                       # takes input for current month,day,year
Cday = int(input('Day:'))
Cyear = int(input('Year:'))

print('Birthday')
Bmonth = int(input('Month:'))                       # takes input for birth month,day,year
Bday = int(input('Day:'))
Byear = int(input('Year:'))

if (Bmonth <= Cmonth) and (Cday < Bday):           # if statement to determine the current age
    age = Cyear - Byear - 1
else:
    age = Cyear - Byear

if (Cmonth == Bmonth) and (Cday == Bday):   # if statement to determine if it's their bday
    print('Happy Birthday!')
    print('You are ', age, 'Years old.')
else:
    print('You are ', age, 'Years old.')
