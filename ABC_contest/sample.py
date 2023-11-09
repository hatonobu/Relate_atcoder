import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,X,Y = mi()

G = [[] for _ in range(N+1)]
for i in range(N-1):
    u,v = mi()
    G[u].append(v)
    G[v].append(u)

ans = []
def dfs2(s,g,used):
    if used[s]:
        return
    else:   
       ans.append(s)
       for nxt in G[s]:
            if nxt == g:
                ans.append(nxt)
                print(*ans)
                exit()
            else:
                used[s] = True
                dfs2(nxt,g,used)
    ans.pop()

used = [False] * (N+1)
dfs2(X,Y,used)