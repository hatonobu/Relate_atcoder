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

N,Q = mi()
P = [input() for _ in range(N)]
ruiseki = [[0] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if P[y][x] == "B":
            ruiseki[y].append(ruiseki[y][-1] + 1)
        else:
            ruiseki[y].append(ruiseki[y][-1])
    
print(ruiseki)

for j in range(Q):
    a,b,c,d = mi()
