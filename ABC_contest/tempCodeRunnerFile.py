import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 10**18

N,M = mi()
G = [[] for _ in range(N)]

for i in range(M):
    u,v = mi()
    u -= 1
    v -= 1
    G[u].append(v)

check = [-1] * N
check2 = [-1] * N
check3 = [-1] * N
q = deque()
q.append((0,0,-1))
check[0] = 0

while(q):
    now,times,flag = q.popleft()
    for nxt in G[now]:
        if nxt == N-1 or nxt == N-2:
            check[nxt] = times+1
            if flag != -1 and flag != nxt:
                pass
            else:
                flag = now
                q.append((nxt,times+1,flag))
                
        else:
            if check[nxt] == -1:
                q.append((nxt,times+1,flag))
                check[nxt] = times + 1
            else:
                check[nxt] = times+1

if check[N-2] != -1:
    q = deque()
    q.append((N-2,0))
    check2[N-2] =  0
    while(q):
        now,times = q.popleft()          
        for nxt in G[now]:
            if check2[nxt] == -1:
                q.append((nxt,times+1))
                check2[nxt] = times + 1
            else:
                check2[nxt] = min(check2[nxt],times+1)
        if now == 0:
            break

if check[N-1] != -1:
    q = deque()
    q.append((N-1,0))
    check3[N-1] =  0
    while(q):
        now,times = q.popleft()
        for nxt in G[now]:
            if check3[nxt] == -1:
                q.append((nxt,times+1))
                check3[nxt] = times + 1
            else:
                check3[nxt] = min(check3[nxt],times+1)
        if now == 0:
            break

ans = INF
if check[N-2] != -1 and check2[0] != -1:
    ans = min(check[N-2] + check2[0],ans)
elif check[N-1] != -1 and check3[0] != -1:
    ans = min(check[N-1] + check3[0],ans)

print(ans if ans != INF else -1)
