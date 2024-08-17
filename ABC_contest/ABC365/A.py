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

Y = ii()

ans = 365
if Y % 4 != 0:
    ans = 365
elif Y % 4 == 0 and Y % 100 != 0:
    ans = 366
elif Y % 100 == 0 and Y % 400 != 0:
    ans = 365
elif Y % 400 == 0:
     ans = 366
    
print(ans)