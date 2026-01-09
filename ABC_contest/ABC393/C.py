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
uv = lli(M)

d = defaultdict(set)

ans = 0
for u,v in uv:
    if u in d[v] and v in d[u]:
        ans += 1
    elif u == v:
        ans += 1
    else:
        d[v].add(u)
        d[u].add(v)

print(ans)