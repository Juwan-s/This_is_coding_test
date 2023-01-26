n, m = map(int, input().split())

nums = list(map(int,input().split()))

min = float('inf')

answer = None

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            print(i, j, k)
            sum = nums[i] + nums[j] + nums[k]

            if abs(m - sum) < min and sum < m:
                min = abs(m - sum)
                answer = sum

print(answer)
