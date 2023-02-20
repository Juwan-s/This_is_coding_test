import sys

while True:
    
    sides = list(map(int, sys.stdin.readline().rstrip().split()))

    sides.sort()

    if sides[0] == 0:
        break

    if sides[-1]**2 == sides[0]**2 + sides[1]**2:
        print('right')
    else:
        print('wrong')