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
A = []
for i in range(N):
    A.append(i+1)
    
rotate = 0
for _ in range(Q):
    X = li()
    if X[0] == 1:
        p,x = X[1],X[2]
        p -= 1
        A[(p+rotate) % N] = x
    elif X[0] == 2:
        p = X[1]
        p -= 1
        print(A[(p+rotate) % N])
    else:
        p = X[1]
        rotate += p

        