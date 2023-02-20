
# N장의 카드가 있음.
# 각 카드는 차례로 1부터 N까지 번호.
# 1번 카드가 제일 위. N번 카드가 제일 아래로 순서대로.

# 다음과 같은 동작을 카드 한장이 남을 때까지 진행
# 1. 제일 위에 있는 카드를 바닥에 버림
# 2. 그 다음 제일 위에 있는 카드를 제일 아래 있는 카드 밑으로 옮김.
# 3. 카드가 한장 남을 때까지 반복

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

nums = [i for i in range(1, N + 1)]

nums = deque(nums)

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums[0])