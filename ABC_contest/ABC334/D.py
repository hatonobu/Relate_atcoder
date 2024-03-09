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
ruiseki = [0]
R = li()
R.sort()
for r in R:
    ruiseki.append(ruiseki[-1] + r)

for i in range(Q):
    num = ii()
    ans = bisect.bisect_right(ruiseki,num)
    print(ans - 1)