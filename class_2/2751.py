import sys

N = int(sys.stdin.readline().rstrip())

nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort()

for i in nums:
    print(i)