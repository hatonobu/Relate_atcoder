import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 8 * 10**18

H,W,N = mi()
dx = defaultdict(set)
dy = defaultdict(set)
for i in range(N):
    x,y = mi()
    dx[x].add(y)
    dy[y].add(x)
Q = ii()

ans = []
for _ in range(Q):
    num, xy = mi()
    if num == 1:
        for n in dx[xy]:
            dy[n].remove(xy)
        ans.append(len(dx[xy]))
        dx[xy].clear()
    elif num == 2:
        for n in dy[xy]:
            dx[n].remove(xy)
        ans.append(len(dy[xy]))
        dy[xy].clear()

print(*ans, sep="\n")  
        