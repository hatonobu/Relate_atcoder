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

N = ii()
L = lli(N)
d = dict()

ans = 0
for i in range(N):
    s,c = L[i]
    times = 0
    while(c > 0):
        if c % 2 == 1:
            n = 2**times * s
            while(1):
                if d.get(n,0) == 1:
                    d.pop(n)
                    n *= 2
                else:
                    break
            d[n] = 1
        c //= 2
        times += 1

print(len(d))

    
