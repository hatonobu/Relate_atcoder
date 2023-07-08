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
P = li()
 
dist = [-1]*N

g = [[] for _ in range(N)]
for i,num in enumerate(P,2):
    g[num-1].append(i-1)

for _ in range(M):
    a,b = mi()
    dist[a-1] = max(dist[a-1],b)

def BFS(s):
    q = deque()
    q.append(s)
    while q:
        num = q.popleft()
        for nxt in g[num]:
            dist[nxt] = max(dist[nxt], dist[num]-1)
            q.append(nxt)
 
BFS(0)
 
Ans = 0
for i in range(N):
    if dist[i] >= 0:
        Ans += 1
 
print(Ans)