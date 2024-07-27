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

N,M = mi()
S = [input() for _ in range(N)]
num = []
for ss in S:
    n = 0
    for i in range(M):
        if ss[i] == "o":
            n += 2**i
    num.append(n)

ans = N
for e in itertools.product(range(2),repeat=N):
    total = 0
    judge = 0
    for i in range(N):
        if e[i] == 1:
            total += 1
            judge |= num[i]
    if judge == 2**M - 1:
        ans = min(ans,total)

print(ans)