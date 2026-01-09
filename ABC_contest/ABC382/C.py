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
A = li()
B = li()
A_lis = []
d = defaultdict(int)
now = INF

for i in range(N):
    num = A[i]
    if now > num:
        A_lis.append(num)
        d[num] = i+1
        now = num

A_lis.sort()

for i in B:
    idx = bisect.bisect_right(A_lis,i)
    if idx == 0:
        print(-1)
    else:
        print(d[A_lis[idx-1]])
