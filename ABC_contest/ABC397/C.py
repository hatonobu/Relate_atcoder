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

check1 = defaultdict(int)
kinds1 = 0
check2 = defaultdict(int)
kinds2 = 0

for i in range(N):
    if check1.get(A[i],-INF) == -INF:
        kinds1 += 1
    check1[A[i]] += 1

ans = 0
for i in range(N):
    check1[A[i]] -= 1
    if check1[A[i]] == 0:
        kinds1 -= 1
    if check2.get(A[i],-INF) == -INF:
        kinds2 += 1
    check2[A[i]] += 1
    
    ans = max(ans,kinds1+kinds2)

print(ans)