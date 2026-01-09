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

N = ii()
qr = lli(N)

Q = ii()
ans = []
for i in range(Q):
    t,d = mi()
    qq,rr = qr[t-1]
    num = (d % qq)
    if num <= rr:
        ans.append((d // qq) * qq + rr)
    else:     
        ans.append(((d // qq) + 1) * qq + rr)

print(*ans,sep="\n")