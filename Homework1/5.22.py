# Mauricio Corado 1254732

print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12')

menu_dict = {"Oil change": 35,            # Created a dictionary with all the set prices that wont change
             "Tire rotation": 19,
             "Car wash": 7,
             "Car wax": 12
             }
# next two lines prompt the user to select the services
serv1 = (input('\nSelect first service:\n'))
serv2 = (input('Select second service:\n'))

print('\nDavy\'s auto shop invoice\n')

# I decided to use If else if to go through all the possible inputs of wanted services

if (serv1 != '-') and (serv2 != '-'):
    print('Service 1: ', serv1, ", $", menu_dict.get(serv1), sep='')
    print('Service 2: ', serv2, ", $", menu_dict.get(serv2), sep='')
    total = menu_dict.get(serv1) + menu_dict.get(serv2)
    print('\nTotal: $', total, sep='')
elif serv1 == '-':
    serv1 = 0
    print('Service 1: No service')
    print('Service 2: ', serv2, ", $", menu_dict.get(serv2), sep='')
    total = serv1 + menu_dict.get(serv2)
    print('\nTotal: $', total, sep='')
elif serv2 == '-':
    serv2 = 0
    print('Service 1: ', serv1, ", $", menu_dict.get(serv1), sep='')
    print('Service 2: No service')
    total = menu_dict.get(serv1) + serv2
    print('\nTotal: $', total, sep='')