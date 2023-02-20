import sys

N = int(sys.stdin.readline().rstrip())

members = []

for i in range(N):
    
    a, b = sys.stdin.readline().rstrip().split()
    members.append([int(a), b, i])

members = sorted(members, key = lambda x : (x[0], x[-1]))

for i, j, k in members:
    print(i, j)