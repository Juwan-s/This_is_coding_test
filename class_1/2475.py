import sys

s = list(map(int, list(sys.stdin.readline().rstrip().split())))

ans = 0


for i in s:
    ans += i**2

print(ans%10)