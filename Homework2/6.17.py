# Mauricio Corado 1254732

# Receives user input
password = input()

# phrase used to replace old with the new
# Replace method was the easiest to use

password = password.replace('i', '!')
password = password.replace('a', '@')
password = password.replace('m', 'M')
password = password.replace('B', '8')
password = password.replace('o', '.')
password = password+'q*s'
print(password)