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

d = dict()

N = ii()
TD = lli(N)
TD.sort()
print(TD)

q = []
heapq.heapify(q)
s = 1
ans = 0
for i in range(N):
    t,d = TD[i]
    if t <= s:
        heapq.heappush(q,t+d+1)
    else:
        while(s < t and q):
            now_t = heapq.heappop(q)
            if s < now_t:
                ans += 1
                s += 1
            else:
                pass
        heapq.heappush(q,t+d+1)

while(q):
    now_t = heapq.heappop(q)
    if s < now_t:
        ans += 1
        s += 1
    else:
        pass

print(ans)
