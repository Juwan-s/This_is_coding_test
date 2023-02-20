# ACM 호텔 문제

# 손님이 도착하는 대로 빈 방 배정

# 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방 선호

# H, W, N의 세 정수를 포함
# H : 호텔의 층 수
# W : 각 층의 객실 수
# N : N번째 손님

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):

    res = None
    cnt = 0
    break_for = False
    H, W, N = list(map(int, sys.stdin.readline().rstrip().split()))
    ans = [[0]*W for i in range(H)]
    for j in range(W):
        for i in range(H):
            cnt += 1
            if cnt == N:
                break_for = True
                res = (i+1, j+1)
        if break_for:
            break
            
    a,b = res
    if b < 10:
        b = '0' + str(b)
    else:
        b = str(b)
    print(str(a)+b)
            







