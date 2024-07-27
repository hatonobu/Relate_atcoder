import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 8 * 10**18

N,M = mi()
A = li()
cost = defaultdict(int)

lis = [INF]*(N+2)
G = [[] for _ in range(N+2)]

for i in range(M):
    x,y,b = mi()
    x -= 1
    y -= 1
    G[x].append(y)
    G[y].append(x)
    cost[(x,y)] = min(cost.get((x,y),INF),b)
    cost[(y,x)] = min(cost.get((y,x),INF),b)

used = [False]*(N+2)
used[0] = True
q = []
heapq.heapify(q)
heapq.heappush(q,(A[0],0))

while(q):
    nowCost,now = heapq.heappop(q)
    if nowCost > lis[now]:
        continue
    for next in G[now]:
        nextCost = nowCost + cost[(now,next)]
        nextCost += A[next]
        if lis[next] > nextCost:
            heapq.heappush(q,(nextCost,next))
            lis[next] = nextCost

print(*lis[1:N])