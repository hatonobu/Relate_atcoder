import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
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
x = [-1] * (N+2)
d = defaultdict(int)

G = [[] for _ in range(N+2)]
for i in range(M):
    u,v,w = mi()
    G[u].append(v)
    G[v].append(u)
    d[(u,v)] = w
    d[(v,u)] = -w

used = [False] * (N+2)
for i in range(1,N+1):
    if used[i] == True:
        pass
    else:
        q = deque()
        q.append(i)
        used[i] = True
        while(q):
            now = q.popleft()
            for nxt in G[now]:
                if used[nxt] == True:
                    continue
                else:
                    q.append(nxt)
                    x[nxt] = x[now] + d[(now,nxt)]
                    used[nxt] = True

print(*x[1:N+1])