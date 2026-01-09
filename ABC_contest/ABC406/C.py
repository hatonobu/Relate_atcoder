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
P = li()
check = [-1] * N
for i in range(N-1):
    if P[i] < P[i+1]:
        check[i] = 2
    elif P[i] > P[i+1]:
        check[i] = 1

ans = 0
start = False
num = 0
for i in range(N-1):
    if check[i] == 1:
        if not start:
            start = True
            ans += max(0, num - 4)
            num = 1
    elif check[i] == 2:
        start = False
        num += 1
        
        