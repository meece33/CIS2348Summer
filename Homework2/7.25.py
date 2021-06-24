# Mauricio Corado 1254732

# defines the function exact change
def exact_change(user_total):
    num_doll = user_total // 100
    user_total %= 100
    num_quar = user_total // 25           # each statement first floor divides to convert to a specific type
    user_total %= 25                      # then modular is used to obtain remainder
    num_dimes = user_total // 10
    user_total %= 10
    num_nick = user_total // 5
    user_total %= 5
    num_penn = user_total
    return num_doll, num_quar, num_dimes, num_nick, num_penn

# statement given by Zylab hint
if __name__ == '__main__':
    input_val = int(input())
    num_doll, num_quar, num_dimes, num_nick, num_penn = exact_change(input_val)
    if input_val <= 0:
        print('no change')

    else:
        if num_doll > 1:                       # each else if statements checks if its singular or plural
            print(num_doll, 'dollars')
        elif num_doll == 1:
            print(num_doll, 'dollar')

        if num_quar > 1:
            print(num_quar, 'quarters')
        elif num_quar == 1:
            print(num_quar, 'quarter')

        if num_dimes > 1:
            print(num_dimes, 'dimes')
        elif num_dimes == 1:
            print(num_dimes, 'dime')

        if num_nick > 1:
            print(num_nick, 'nickels')
        elif num_nick == 1:
            print(num_nick, 'nickel')

        if num_penn > 1:
            print(num_penn, 'pennies')
        elif num_penn == 1:
            print(num_penn, 'penny')