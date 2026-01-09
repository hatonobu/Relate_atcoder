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
P = li()

r = 1
lis = [-1] * (N)
for i in range(N):
    m = -1
    for j in range(N):
        if lis[j] == -1:
            m = max(m, P[j])
    if m != -1:
        num = 0
        for k in range(N):
            if P[k] == m:
                lis[k] = r
                num += 1
        r += num
    if m == -1:
        break

print(*lis,sep="\n")