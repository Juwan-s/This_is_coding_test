import sys

s1 = list(sys.stdin.readline().rstrip())
s2 = []

N = int(sys.stdin.readline().rstrip())
"""
두개의 list로 쪼개어서 사용하는데, 그 사이를 커서로 두겠다는 intuition
"""
for _ in range(N):
    cmd = list(sys.stdin.readline().rstrip().split())

    if cmd[0] == 'L': # 만약 왼쪽커서의 이동이라면,
        if s1: # 커서 왼쪽이 남아있는 경우
            s2.append(s1.pop()) # 커서 왼쪽의 것을 빼서 두번째에 넣는다.
                                # 이때 주의할 점은 s2는 스택구조를 유지한다는 것.

    elif cmd[0] == 'D': # 만약 오른쪽으로의 커서 이동이라면
        if s2:          # 커서 오른쪽이 남아 있는 경우에만 사용
            s1.append(s2.pop())
    
    elif cmd[0] == 'B': # 버리는 연산의 경우 간단하게 pop만 해주면 된다.
        if s1:
            s1.pop()
    
    else:
        s1.append(cmd[1]) # 추가의 경우에도 간단하게 구현할 수 있다.

s1.extend(reversed(s2)) # s2가 스택 구조로 되어있었기 때문에
                        # 이를 역전시켜 이어준다.
print(''.join(s1))
