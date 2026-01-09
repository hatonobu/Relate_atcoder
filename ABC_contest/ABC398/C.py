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


d = defaultdict(int)
set_A = set()

for i in range(N):
    if d.get(A[i],-INF) == -INF:
        d[A[i]] = 1
    else:
        d[A[i]] += 1    
        set_A.add(A[i])

ans = -1
now = -1
for i in range(N):
    if A[i] in set_A:
       pass
    else:
        if now < A[i]:
            now = A[i]
            ans = i + 1

print(ans)
        