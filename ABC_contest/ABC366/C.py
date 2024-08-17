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

Q = ii()
d = defaultdict(int)

ans = []
for i in range(Q):
    n = li()
    if n[0] == 3:
        ans.append(len(d))
    else:
        num, x = n[0],n[1]
        if num == 1:
            d[x] += 1
        else:
            d[x] -= 1
            if d[x] == 0:
                del d[x]

print(*ans,sep="\n")