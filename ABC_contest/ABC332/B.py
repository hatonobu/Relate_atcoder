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

K,G,M = mi()
g = 0
m = 0
for i in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        num = G - g
        if num > m:
            g += m
            m = 0
        else:
            g = G
            m -= num

print(g,m)