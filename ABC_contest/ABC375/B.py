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

N = ii()
total = 0

now = (0,0)
for i in range(N):
    x,y = mi()
    nx,ny = now[0],now[1]
    total += math.sqrt((nx-x)**2 + (ny-y)**2)
    now = (x,y)

nx,ny = now[0],now[1]
total += math.sqrt((nx)**2 + (ny)**2)
print(total)