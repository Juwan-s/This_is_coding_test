import sys

N = int(sys.stdin.readline())

my_stack = []

for i in range(N):
    
    inp = sys.stdin.readline().rstrip()

    if 'push' in inp:
        b = int(inp.split()[-1])
        my_stack.append(b)
        continue

    if inp == 'top':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack[-1])

    elif inp == 'size':
        print(len(my_stack))

    elif inp == 'pop':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack.pop())
    else:
        if len(my_stack) == 0:
            print(1)
        else:
            print(0)