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

N, D = map(int, input().split())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())
M = 2 * 10**6


def calc(xs):
    xsum = [0] * (2 * M + 1)
    xs.sort()
    i = 0
    xsum[-M] = sum(xs) + N * M
    for x in range(-M + 1, M + 1):
        while i < N and xs[i] < x:
            i += 1
        xsum[x] = xsum[x - 1] + 2 * i - N
    return xsum


xsum = calc(x)
ysum = calc(y)
xsum.sort()
ysum.sort()
ans = 0
j = 0
for i in range(2 * M + 1)[::-1]:
    while j < 2 * M + 1 and xsum[i] + ysum[j] <= D:
        j += 1
    ans += j
print(ans)

