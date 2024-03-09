import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

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

ans = 0
d = defaultdict(int)
q = []
heapq.heapify(q)
N = ii()

heapq.heappush(q,-N)
check = set()
check.add(0)
check.add(1)
d[-N] += 1

while(q):
    n = -heapq.heappop(q)
    a,b = -math.floor(n/2), -math.ceil(n/2)
    d[a] += d[-n]
    d[b] += d[-n]
    if a == b :
        if not a in check:
            heapq.heappush(q,a)
    else:
        if not a in check:
            heapq.heappush(q,a)
        if not b in check:
            heapq.heappush(q,b)
    check.add(a)
    check.add(b)

for a,b in d.items():
    if a < -1:
        ans += -a*b

print(ans)
