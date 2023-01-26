import sys
from collections import deque


def is_valid(ps):

    deq = deque(ps)
    s = []

    if len(deq) < 2:
        return 'NO'

    while deq:
        
        a = deq.popleft()
        if a == '(':
            s.append(a)
            continue
        elif a == ')':
            try:
                s.pop()
            except:
                return 'NO'

    return 'YES' if len(s) == 0 else 'NO'


N = int(sys.stdin.readline().rstrip())

for _ in range(N):

    ps = list(input())
    print(is_valid(ps))