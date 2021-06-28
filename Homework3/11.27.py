# Mauricio Corado 1254732

players = dict()

count = 0
while count < 5:
    jers_num = int(input("Enter player {}'s jersey number:\n".format(count+1)))
    rating = int(input("Enter player {}'s rating:\n".format(count+1)))
    print('')
    players[jers_num] = rating
    count = count + 1

print('ROSTER')
for i in sorted(players):
    print('Jersey number: {}, Rating: {}'.format(i, players[i]))


while(1):
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
        for i in sorted(players):
            if players[i] > rating:
                print("\n\nABOVE {}".format(rating))
    elif command == 'o':
        for i in sorted(players):
            print('Jersey number: {}, Rating: {}'.format(i, players[i]))
    else:
        exit(0)