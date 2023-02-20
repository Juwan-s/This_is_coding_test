import sys

K, N = map(int, sys.stdin.readline().rstrip().split())

lans = []

for _ in range(K):
    lans.append(int(sys.stdin.readline().rstrip()))

lo = 1
hi = max(lans)

while lo <= hi: # 이분 탐색을 진행
    mid = (lo + hi) // 2 # 중앙값 선정. 반으로 나누어야 최소 2개씩은 만들 수 있다.
    cnt  = 0 # 
    for i in range(K): # 지금 갖고 있는 랜선들
        cnt += lans[i] // mid # 갖고 있는 랜선들을 기준으로 1씩 줄여가면서 자름
    if cnt >= N: # 만약 나온 개수가 N보다 많으면
        lo = mid + 1 # 상한을 높여서 N개에 거의 가깝게 뽑도록 함
    else:
        hi = mid - 1 # # 만약 개수가 모자르면 1씩 감소시켜 개수를 조금 더 줄이도록 함
    
print(hi)