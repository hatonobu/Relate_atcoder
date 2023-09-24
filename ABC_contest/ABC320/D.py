import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,M = mi()
d = dict()
d[1] = (0,0)
va = [[] for _ in range(N+1)]
vb = [[] for _ in range(N+1)]

for i in range(M):
    a,b,x,y = mi()
    va[a].append((b,x,y))
    vb[b].append((a,x,y))

q = deque([1])
used = [False]*(N+1)

while(q):
    pos = q.popleft()
    pos_x, pos_y = d[pos]
    if used[pos]:
        continue
    else:
        for S1 in va[pos]:
            next,x,y = S1
            q.append(next)
            d[next] = (pos_x + x, pos_y + y)

        for S2 in vb[pos]:
            next,x,y = S2
            q.append(next)
            d[next] = (pos_x - x, pos_y - y)
    used[pos] = True

for i in range(1,N+1):
    if d.get(i,0):
        x,y = d[i]
        print(x,y)
    else:
        print("undecidable")
