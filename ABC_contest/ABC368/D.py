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

N,K = mi()
AB = lli(N-1)
V = li()
for i in range(K):
    V[i] -= 1
start = V[0]
V = set(V)

G = [set() for _ in range(N)]

for a,b in AB:
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)

deg = []
q = []
for i,n in enumerate(G):
    if len(n) == 1:
        q.append(i)

ans = N
for now in q:
    if now in V:
        continue
    else:
        nxt = G[now].pop()
        G[nxt].discard(now)
        ans -= 1
        if len(G[nxt]) == 1:
            q.append(nxt)

print(ans)