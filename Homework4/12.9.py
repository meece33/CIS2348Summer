# 1254732 Mauricio Corado

user_input = input().split()     # splits the user input
name = user_input[0]            # set the first part of the split into name
age = user_input[1]         # second part of the input is age

while name != '-1':     # loo[ that runs until value is -1
    try:
        age = int(user_input[1]) + 1
    except ValueError:
        age = 0
    print('{} {}'.format(name, age))
    user_input = input().split()
    name = user_input[0]