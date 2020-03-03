for i in range(1, 21, 2):
    print(i, end=' ')
print()

for t in range(0, 101, 10):
    print(t, end=' ')
print()

for x in range(20, 0, -1):
    print(x, end=' ')
print()

STARS = int(input('Enter the amount of stars you want: '))

for x in range(STARS):
    print("*", end='')
print()

for z in range(STARS + 1):
    for j in range(z):
        print("*", end=' ')
    print()
