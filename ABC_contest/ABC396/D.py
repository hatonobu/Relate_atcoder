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

#dfs
G = [[] for _ in range(N)]

for i in range(M):
    u,v,w = mi()
    G[u-1].append((v-1,w))
    G[v-1].append((u-1,w))

used = [False]*N
ans = INF

def dfs(v,used,num):
    global ans
    if v == N-1:
        ans = min(ans,num)
    else:
        for next_v,w in G[v]:
            if not used[next_v]:
                used[next_v] = True
                dfs(next_v,used,num^w)
                used[next_v] = False

used[0] = True
dfs(0,used,0)
print(ans)