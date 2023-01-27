import sys

N = sys.stdin.readline()

nums = list(map(int, list(sys.stdin.readline().rstrip().split())))

m = max(nums)

ans = []

for i in nums:
    ans.append(i/m*100)

print(sum(ans)/len(ans))