import sys

from collections import Counter

s = list(sys.stdin.readline().rstrip().upper())

if len(s) == 1:
    print(s[0])

else:
    cnt = Counter(s)

    a, b = cnt.most_common(2)

    print(a[0]) if a[1] > b[1] else print('?')