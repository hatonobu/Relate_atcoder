#TLE,WA
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
V = [[] for _ in range(N+1)]
for i in range(M):
    u,v = mi()
    if A[u-1] >= A[v-1]:
        V[v].append(u)
    if A[v-1] >= A[u-1]:
        V[u].append(v)


ans = 0
def dfs(s,d):
    global ans
    n = 0
    d[A[s-1]] += 1
    if s == N:
        #print("answer")
        ans = max(ans,len(d))
    else:   
       for nxt in V[s]:
            if used[nxt]:
                ans = max(ans,len(d)+used[nxt])
                d.clear()
                return 0
            else:
                used[nxt] = -1
                n = dfs(nxt,d)
    used[s] = max(0,n - len(d),used[s])
    d[A[s-1]] -= 1
    if d[A[s-1]] == 0:
        del d[A[s-1]]
    return 0

used = [0] * (N+1)
for i in range(1,N):
    if used[i] == 0:
        d = defaultdict(int)
        dfs(i,d)

print(ans)