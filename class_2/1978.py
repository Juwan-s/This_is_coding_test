import sys

# 1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
# 2. 2부터 시작해서 나열된 수에서 지워지지 않은 수 중 가장 작은 2를 소수로 선택하고 2의 배수를 지운다
# 3. 3도 지워지지 않았기 때문에 소수로 선택하고 3의 배수를 지운다.
# 4. 4는 지워졌기 때문에 넘어가고 5를 소수로 선택하고 5의 배수를 지운다.
# 5. 2,3,4를 반복
# 6. 반복이 끝나면 지워지지 않은 것들이 소수


N = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().rstrip().split()))

n = max(nums)

a = [True]*(n + 1)

m = int(n**0.5)

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, n + 1, i):
            a[j] = False

a[0], a[1] = False, False

cnt = 0

for i in nums:
    if a[i] == True:
        cnt += 1

print(cnt)