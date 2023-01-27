import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    cmd = list(sys.stdin.readline().rstrip().split())
    ans = ''

    for i in list(cmd[1]):
        ans += i*int(cmd[0])

    print(ans)