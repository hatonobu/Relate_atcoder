import sys
from collections import deque, defaultdict
import itertools
import heapq
import bisect
import queue

# sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 8 * 10**18

N, R = mi()
L = li()

ans = 0
check = True
for i in range(R):
    if L[i] == 0:
        ans += 1
        check = False
    else:
        if check:
            continue
        ans += 2

check = True
for j in range(N - 1, R - 1, -1):
    if L[j] == 0:
        ans += 1
        check = False
    else:
        if check:
            continue
        ans += 2

print(ans)