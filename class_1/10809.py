import string
import sys

s = list(sys.stdin.readline().rstrip().lower())
asc = set(list(string.ascii_lowercase))
d = {}
for idx, i in enumerate(s):
    if i not in d:
        d[i] = idx

for i in string.ascii_lowercase:
    print(d[i], end=' ') if i in d else print(-1, end=' ')