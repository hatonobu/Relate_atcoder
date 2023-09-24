import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,M = mi()

G = [ [ ] for _ in range(N+1)]

for i in range(M):
    u,v = mi()
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

check = [0]*(N+1)
used = [False]*(N+1)

#dfs
ans = N * (N-1) // 2 - M
for i in range(N):
    if used[i]:
        continue
    q = deque([i])
    check[i] = 1
    cnt = [0,1,0]
    while(q):
        now = q.pop()
        for next in G[now]:
            if used[next]:
                if check[next] == check[now]:
                    print(0)
                    exit()
            else:
                check[next] = -check[now]
                cnt[check[next]] += 1
                q.append(next)
        used[now] = True
    
    print(ans,i)
    print(cnt)
    ans -= cnt[1] * (cnt[1] - 1) // 2
    ans -= cnt[-1] * (cnt[-1] - 1) // 2

print(ans)



    
