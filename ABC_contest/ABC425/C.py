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

N,Q = mi()
A = li()
ruiseki = [0]*(N+1)
for i in range(N):
    ruiseki[i+1] = ruiseki[i] + A[i]

look_start = 0
for _ in range(Q):
    l = li()
    if l[0] == 1:
        c = l[1]
        look_start = (look_start + c) % N
    elif l[0] == 2:
        l,r = l[1],l[2]
        l = (l - 1 + look_start) % N
        r = (r - 1 + look_start) % N
        if l <= r:
            print(ruiseki[r+1] - ruiseki[l])
        else:
            print(ruiseki[N] - ruiseki[l] + ruiseki[r+1])