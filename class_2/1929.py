import sys

# 에라토스테네스의 체에 관한 문제

a, b = map(int, sys.stdin.readline().rstrip().split())

nums = []

# 1은 소수가 아님으로 약속
# 배열을 생성하고 초기화
for i in range(a, b+1):
    nums.append(i)

# 2부터 시작해서 특정 수의 배수에 해당하는 수는 지움

for i in range(2, b+1):
    if nums[i] == 0:
        continue
    
    for j in range(2*i, b+1, i): # 최소 2배수부터 시작하여 i의 배수가 되는 것을 다 지움
        if j < b-a:
            nums[j] = 0

for i in range(2, b+1):
    print(nums[i], end=' ') if nums[i] != 0 else print('', end='')