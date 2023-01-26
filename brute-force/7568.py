from collections import defaultdict

N = int(input())

p = []

cnt = {}


for i in range(N):
    a, b = map(int,input().split())
    p.append([a, b])
    if (a, b) not in cnt:
        cnt[(a,b)] = 0

for i in range(N):
    for j in range(N):
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            cnt[(p[i][0], p[i][1])] += 1

for i in p:
    print(cnt[(i[0], i[1])], end=' ')
print()