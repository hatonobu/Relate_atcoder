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

N,Q = mi()
now = [1,2]

ans = 0
for i in range(Q):
    h,y = ml()
    y = int(y)
    if h == "L":
        if now[0] == y:
            continue
        elif now[0] < y:
            if now[0] < now[1] < y:
                ans += now[0] + N-y
            else:
                ans += y - now[0]
        else:
            if y < now[1] < now[0]:
                ans += N-now[0] + y
            else:
                ans += now[0] - y
        now[0] = y
    else:
        if now[1] == y:
            continue
        elif now[1] < y:
            if now[1] < now[0] < y:
                ans += now[1] + N-y
            else:
                ans += y - now[1]
        else:
            if y < now[0] < now[1]:
                ans += N-now[1] + y
            else:
                ans += now[1] - y
        now[1] = y

print(ans)