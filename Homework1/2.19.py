# Mauricio Corado ID: 1254732

lemon = float(input('Enter amount of lemon juice (in cups):\n'))

water = float(input('Enter amount of water (in cups):\n'))

agave = float(input('Enter amount of agave nectar (in cups):\n'))      # gathers input & formats it as a float

servings = float(input('How many servings does this make?\n'))


# next 4 lines prints and formats the user input
print('\nLemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar\n')

Idealservings = float(input('How many servings would you like to make?\n'))

# next 3 lines is where all the calculations are done

lemon = ((Idealservings/servings) * lemon)
water = ((Idealservings/servings) * water)
agave = ((Idealservings/servings) * agave)

print('\nLemonade ingredients - yields', '{:.2f}'.format(Idealservings), 'servings')
print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar')

print('\nLemonade ingredients - yields', '{:.2f}'.format(Idealservings), 'servings')

# converts to gallons

lemon = lemon/16
water = water/16
agave = agave/16

print('{:.2f}'.format(lemon), 'gallon(s) lemon juice')
print('{:.2f}'.format(water), 'gallon(s) water')
print('{:.2f}'.format(agave), 'gallon(s) agave nectar')