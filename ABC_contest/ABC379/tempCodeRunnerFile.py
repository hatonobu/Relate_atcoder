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

N,M = mi()
X = li()
A = li()

now = 1
ans = 0

for i in range(M):
    if now < X[i]:
        print(-1)
        exit()
    else:
        now += A[i]
        ans += ((A[i]-1) * A[i]) // 2

if now == N+1:
    print(ans)
else:
    print(-1)