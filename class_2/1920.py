import sys

N = int(sys.stdin.readline().rstrip())

a = []

def bs(arr, t):
    lo = 0
    hi = len(arr)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == t:
            return True
        elif arr[mid] > t:
            hi = mid - 1
        else:
            lo = mid + 1


a = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()

M = int(sys.stdin.readline().rstrip())

b = list(map(int, sys.stdin.readline().rstrip().split()))

ans = []

for c in b:

    ans.append(1) if bs(a, c) == True else ans.append(0)

for i in ans:
    print(i, end=' ')
    
