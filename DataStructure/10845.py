import sys

from collections import deque

N = int(sys.stdin.readline().rstrip())

q = deque()

for _ in range(N):

    cmd = list(sys.stdin.readline().rstrip().split())

    if cmd[0] == 'push':
        q.append(cmd[1])

    elif cmd[0] == 'pop':
        print(q.popleft()) if len(q) != 0 else print(-1)

    elif cmd[0] == 'size':
        print(len(q))

    elif cmd[0] == 'empty':
        print(1) if len(q) == 0 else print(0)

    elif cmd[0] == 'front':
        print(q[0]) if len(q) != 0 else print(-1)

    else:
        print(q[-1]) if len(q) != 0 else print(-1)



