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

N = ii()
A = li()

lis_left = [-1]*(10**6+2)
lis_right = [-1]*(10**6+2)
max_dp_num = [-1]*(N+2)

d = defaultdict(int)

dp = [0]*N

ans = INF
for i in range(N):
    if d.get(A[i],-INF) == -INF:
        d[A[i]] = 0
        lis_left[A[i]] = i
    else:
        lis_right[A[i]] = i
        ans = min(ans, lis_right[A[i]]-lis_left[A[i]]+1)

print(ans if ans != INF else -1)