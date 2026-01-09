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
L = li()

s = 0
g = N
for i in range(N):
    if L[i] == 0:
        s += 1
    else:
        break

for j in range(N-1,-1,-1):
    if L[j] == 0:
        g -= 1
    else:
        break
    
if s >= g:
    print(0)
else:
    print(g-s-1)