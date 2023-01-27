import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):

    s = list(sys.stdin.readline().rstrip())
    c = 0
    ans = 0
    for i in s:

        if i == 'O':
            c += 1
            ans += c
        else:
            c = 0

    print(ans)


            
    