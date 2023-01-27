import sys
from collections import Counter
n = 1
for _ in range(3):
    n *= int(sys.stdin.readline().rstrip())
cnt = Counter(list(str(n)))
for i in range(0, 10):
    print(cnt[str(i)])