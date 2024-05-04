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
XY = lli(N)

for i in range(N):
    x1,y1 = XY[i]
    total = -1
    ans = -1
    for j in range(N):
        if i == j:
            continue
        x2,y2 = XY[j]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2
        if total < dist:
            total = dist
            ans = j
    print(ans+1)
