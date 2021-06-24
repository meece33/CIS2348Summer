# Mauricio Corado 1254732


# takes input for the coefficients of both equations

a = int(input())
b = int(input())
c = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

solution = 0

for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if (a * x + b * y == c) and (a2 * x + b2 * y == c2):
            print(x, y)
            solution = 1
# if solution has not been found i.e not equal to 1 as it would be assigned
if solution != 1:
    print("No solution")