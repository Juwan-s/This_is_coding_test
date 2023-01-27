import sys
from collections import Counter

l = []

for _ in range(10):
    l.append(int(sys.stdin.readline().rstrip()) % 42)

cnt = Counter(l)

print(len(cnt))