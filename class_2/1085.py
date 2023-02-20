import sys
x, y, w, h = map(int, list(sys.stdin.readline().rstrip().split()))
print(min(x-0, w-x, y-0, h-y))