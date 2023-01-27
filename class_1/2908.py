import sys
s = list(sys.stdin.readline().rstrip().split())
a = int(''.join(reversed(s[0])))
b = int(''.join(reversed(s[1])))
print(max(a, b))