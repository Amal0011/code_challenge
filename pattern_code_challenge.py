import math
# reading the inputs
r = int(input("inputs :- "))
c = int(input())

for m in range(math.ceil(c / 2)):
    print(" ___", end='    ')
print()

for i in range(r):
    for j in range(math.ceil(c / 2)):
        print("/", end='   ')
        print(chr(92), end='')
        if j < math.ceil(c / 2) - 1 or c % 2 == 0 :
            print("___", end='')
        if j == math.ceil(c / 2) - 1 and c % 2 == 0 and i != 0:
            print('/', end='')
    print()
    for j in range(math.ceil(c / 2)):
        print(chr(92), end='')
        print("___", end='')
        print("/", end='   ')     
        if j == math.ceil(c / 2) - 1 and c % 2 == 0 and i != r - 1:
            print(chr(92), end='')
    print()

