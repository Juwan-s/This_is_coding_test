import sys


while True:
    a = sys.stdin.readline().rstrip()
    if a == '0':
        break
    a = list(a)

    print('yes') if a == a[::-1] else print('no')

    