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

N,S,M,L = mi()

ans = 10**18
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            total = 6*i + 8*j + 12*k
            if total >= N:
                ans = min(ans,S*i + M*j + L*k)

print(ans)