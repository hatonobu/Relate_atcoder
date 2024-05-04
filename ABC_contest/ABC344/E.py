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
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 10**18

d = defaultdict(list)
N = ii()
A = li()
Q = ii()
if N == 1:
    d[A[0]] = [-1,INF]
else:
    for i in range(N):
        if i == 0:
            d[A[i]] = [-1,A[i+1]]
        elif i == N-1:
            d[A[i]] = [A[i-1],INF]
        else:
            d[A[i]] = [A[i-1],A[i+1]]

s = A[0]
for i in range(Q):
    l = li()
    if l[0] == 1:
        x,y = l[1],l[2]
        d[y] = [x,d[x][1]]
        if d[x][1] != INF:
            d[d[x][1]][0] = y
        d[x][1] = y        
    else:
        x = l[1]
        lis = d[x]
        if lis[0] != -1:
            d[lis[0]][1] = lis[1]
        if lis[1] != INF:
            d[lis[1]][0] = lis[0]
            if lis[0] == -1:
                s = lis[1]
        del d[x]

ans = []
ans.append(s)
nxt = d[s][1]
while(1):
    if nxt == INF:
        break
    ans.append(nxt)
    nxt = d[nxt][1]

print(*ans)
