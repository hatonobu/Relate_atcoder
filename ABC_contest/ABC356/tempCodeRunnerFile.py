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

N,M,K = mi()
check = []

for e in itertools.product(range(2),repeat=N):
    check.append(e)

for i in range(M):
    nxt = []
    see = []
    C = li_st()
    for n in C[1:-2]:
        see.append(int(n)-1)
    for e in check:
        if C[-1] == "o":
            total = 0
            for num in see:
                if e[num] == 1:
                    total += 1
            if total >= K:
                nxt.append(e)
        else:
            total = 0
            for num in see:
                if e[num] == 1:
                    total += 1
            if total < K:
                nxt.append(e)
    check = nxt

print(len(check))
