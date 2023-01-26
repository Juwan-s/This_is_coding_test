from collections import deque

N = int(input())

def is_valid(arr):

    s = []
    ans = []
    cnt = 1

    for i in arr:
        
        while cnt <= i:
            s.append(cnt)
            ans.append('+')
            cnt += 1

        if s[-1] == i:
            s.pop()
            ans.append('-')
        else:
            return 'NO'
    
    return ans

nums = []

for _ in range(N):
    nums.append(int(input()))

res = is_valid(nums)

if res != 'NO':
    for i in res:
        print(i)
else:
    print(res)