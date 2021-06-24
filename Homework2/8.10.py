# Mauricio Corado 1254732

user_input = input()             # takes in input

no_spaces = user_input.replace(" ", "")           # replaces spaces with no spaces
rev = ''.join(reversed(no_spaces))                # reversed the no spaced string

# if statement to determine if indeed the string is a palindrome
if no_spaces == rev:
    print(user_input, 'is a palindrome')
else:
    print(user_input, 'is not a palindrome')
