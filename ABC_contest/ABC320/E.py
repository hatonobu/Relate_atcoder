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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,M = mi()
T = lli(M)
ans = [0]*N
row = list(range(N))
event = []
heapq.heapify(event)
heapq.heapify(row)

#-1でそうめん、それ以外帰宅
for i in range(M):
    t,w,s = T[i]
    heapq.heappush(event,((t,w,s,-1)))

while(event):
    t,w,s,p = heapq.heappop(event)
    if p == -1:
        if row:
            b = heapq.heappop(row)
            ans[b] += w
            heapq.heappush(event,(t+s,-1,-1,b))
    else:
        heapq.heappush(row,p)

print(*ans,sep="\n")