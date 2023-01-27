import sys

class Node:
    def __init__(self, data, Next=None):
        self.data = data
        self.next = Next

N, K = map(int, list(sys.stdin.readline().rstrip().split()))

linked = set()

globals()['n{}'.format(N)] = Node(N)

for i in range(N-1, 0, -1):
    globals()['n{}'.format(i)] = Node(i)
    globals()['n{}'.format(i)].next = globals()['n{}'.format(i+1)]

    linked.add(globals()['n{}'.format(i)])

globals()['n{}'.format(N)].next = globals()['n{}'.format(1)]
linked.add(globals()['n{}'.format(N)])

hop = 1
pnt = n1
ans = []

while linked:

    hop += 1

    if hop == K:
        linked.remove(pnt.next)
        ans.append(pnt.next.data)
        pnt.next = pnt.next.next
        hop = 0
    else:
        pnt = pnt.next

print('<', ', '.join(list(map(str, ans))), '>', sep='')