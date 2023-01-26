import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

for _ in range(N):

    a = list(sys.stdin.readline().rstrip().split())

    for i in a:
        temp = list(i)
        while temp:
            print(temp.pop(), end='')
        print(' ', end='')