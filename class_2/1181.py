import sys

N = int(sys.stdin.readline().rstrip())

words = set()

for i in range(N):
    word = sys.stdin.readline().rstrip()
    words.add((len(word), word))
    
words = list(words)
words.sort(key = lambda x : (x[0], x[1]))

for i, j in words:
    print(j)