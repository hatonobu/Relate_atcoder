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

A,M,L,R = mi()
left = min(L,R)
right = max(L,R)

if A <= left:
    if (left - A) % M == 0:
        start = A + ((left - A) // M )* M
    else:
        start = A + ((left - A) // M + 1) * M
else:
    #print(A - left)
    start = A - ((A - left) // M) * M

#print(start,right)
if not left <= start <= right:
    print(0)
else:
    print((right - start) // M + 1)