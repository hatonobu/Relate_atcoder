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
mod = 10**9
INF = 8 * 10**18

N,K = mi()

total = 0
lis = []
for i in range(N+1):
    if len(lis) < K:
        lis.append(1)
    else:
        lis.append(total)
        total -= lis[i-K]
    total += lis[-1]
    
    total %= mod

print(lis[N])
    