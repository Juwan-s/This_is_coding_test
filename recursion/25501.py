n = int(input())

def rec(s, l, r, d):

    if l >= r: return 1, d+1
    elif s[l] != s[r]: return 0, d+1
    else: return rec(s, l+1, r-1, d+1)


def isPalindrome(s):
    return rec(s, 0, len(s)-1, 0)

for _ in range(n):

    s = input()
    print(isPalindrome(s)[0], isPalindrome(s)[1])








