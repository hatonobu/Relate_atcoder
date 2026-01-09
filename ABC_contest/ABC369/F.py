import sys
from collections import deque,defaultdict
import pypyjit
import itertools
import heapq
import bisect
import queue

pypyjit.set_param("max_unroll_recursion=-1")
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
plate = [[-1]*(W+3) for _ in range(H+3)]
check = set()
for i in range(N):
    r,c = mi()
    check.add((r,c))

sx,sy = 1,1
q = deque()
q.append((sx,sy))
while(q):
    nx,ny = mi()
