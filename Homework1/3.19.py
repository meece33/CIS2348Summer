import math


height = int(input('Enter wall height (feet):\n'))               # input statements for width and height
width = int(input('Enter wall width (feet):\n'))

area = width * height                                    # formula for area base*height
print('Wall area:', area, 'square feet')

paintNeed = area / 350
print('Paint needed:', '{:.2f}'.format(paintNeed), 'gallons')

cansNeed = math.ceil(paintNeed)                    # establishes the cans needed
print('Cans needed:', cansNeed, 'can(s)')

colorDict = {"red": 35,                 # created a dictionary with the proper prices for each color
             "blue": 25,
             "green": 23}

color = (input('\nChoose a color to paint the wall:\n'))
colorChoice = colorDict.get(color)
cost = cansNeed * colorChoice

print('Cost of purchasing ', color, ' paint: $', cost, sep='')