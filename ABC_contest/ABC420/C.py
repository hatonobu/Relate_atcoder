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
INF = 8 * 10**18

N,Q = mi()
A = li()
B = li()
cXV = [li_st() for _ in range(Q)]
min_lis = [0]*N
for i in range(N):
    min_lis[i] = min(A[i],B[i])
ans = sum(min_lis)

for i in range(Q):
    c,x,v = cXV[i]
    x = int(x)
    v = int(v)
    if c == "A":
        ans -= min_lis[x-1]
        A[x-1] = v
        min_lis[x-1] = min(A[x-1],B[x-1])
        ans += min_lis[x-1]
    else:
        ans -= min_lis[x-1]
        B[x-1] = v
        min_lis[x-1] = min(A[x-1],B[x-1])
        ans += min_lis[x-1]
    print(ans)