import sys

a = int(sys.stdin.readline().rstrip())

cnt = 0
temp = -1

while True:
    temp += 1

    if '666' in str(temp):
        cnt += 1
        if cnt == a:
            print(temp)
            break