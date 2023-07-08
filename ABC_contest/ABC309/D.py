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

from collections import deque,defaultdict

def BFS(s,N,uf):
    dist = [-1] * N
    dist[s] = 0
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        for nxt in uf[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    return dist
    
N1,N2,M = mi()
g1 = [[] for _ in range(N1)]
g2 = [[] for _ in range(N2)]

for i in range(M):
    i,j = mi()

    if i <= N1:
        g1[i-1].append(j-1)
        g1[j-1].append(i-1)
    else:
        g2[i-N1-1].append(j-N1-1)
        g2[j-N1-1].append(i-N1-1)

dist_from_zero = BFS(0,N1,g1)
dist_from_zero2 = BFS(N2-1,N2,g2)

a = max(dist_from_zero)
b = max(dist_from_zero2)

print(a + b + 1)
