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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,X = mi()
A = li()
total = sum(A)
A.sort()
total -= A[-1]
m = A[0]


ans = 0
if total >= X:
    ans = 0
else:
    total -= m
    ans = max(X-total,0)
    if ans > A[-1]:
        ans = -1

print(ans)
