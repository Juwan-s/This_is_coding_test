import sys

N, M = map(int, list(sys.stdin.readline().rstrip().split()))

board = []

ans = []

for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

for x in range(N-7): # 8칸
    for y in range(M-7):
        w = 0 # 첫 칸이 W일 경우
        b = 0 # 첫 칸이 B일 경우
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j) % 2 == 0: # 만약 행과 열의 합이 짝수가 아니라면 시작점의 색과 동일해야한다.
                    if board[i][j] != 'W':
                        w += 1
                    if board[i][j] != 'B':
                        b += 1
                else:
                    if board[i][j] != 'B':
                        w += 1
                    if board[i][j] != 'W':
                        b += 1
        ans.append(min(w, b))

print(min(ans))