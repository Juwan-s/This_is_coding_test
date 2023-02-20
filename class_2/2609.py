import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

x, y =  list(map(int, sys.stdin.readline().rstrip().split()))

print(gcd(x,y))
print(lcm(x,y))