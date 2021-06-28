# Mauricio Corado 1254732

players = dict()        # creates an empty Dict

count = 0
while count < 5:            # while loop is used in order to populate the players dictionary
    jers_num = int(input("Enter player {}'s jersey number:\n".format(count+1)))
    rating = int(input("Enter player {}'s rating:\n".format(count+1)))
    print('')
    players[jers_num] = rating
    count = count + 1

print('ROSTER')             # this section prints out the complete sorted roster
for i in sorted(players):
    print('Jersey number: {}, Rating: {}'.format(i, players[i]))


while(1):                   # Big while loop is used to run the menu option. Will exit until q is selected
    print('\nMENU')
    print('a - Add player\n'
    'd - Remove player\n'
    'u - Update player rating\n'
    'r - Output players above a rating\n'
    'o - Output roster\n'
    'q - Quit\n')

    command = (input('Choose an option:\n'))

    if command == 'a':
        print("Enter a new player's jersey number:")
        jers_num = int(input())
        print("Enter a new player's jersey number:")
        rating = int(input())
        players[jers_num] = rating
    elif command == 'd':
        print("Enter a jersey number:\n")
        jers_num = int(input())
        players.pop(jers_num)
    elif command == 'u':
        print("Enter a jersey number:\n")
        jers_num = int(input())
        print("Enter a new rating for player:\n")
        rating = int(input())
        players[jers_num] = rating
    elif command == 'r':
        print("Enter a rating:\n")
        rating = int(input())
        print("\n\nABOVE {}".format(rating))
        for i in sorted(players):
            if players[i] > rating:
                print('Jersey number: {}, Rating: {}'.format(i, players[i]))
    elif command == 'o':
        print('ROSTER')
        for i in sorted(players):
            print('Jersey number: {}, Rating: {}'.format(i, players[i]))
    else:
        exit(0)