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

N,C = mi()
T = li()

now = -1
ans = 0
for i in range(N):
    if now == -1:
        ans += 1
        now = i
    else:
        if T[i] - T[now] >= C:
            ans += 1
            now = i

print(ans)
            