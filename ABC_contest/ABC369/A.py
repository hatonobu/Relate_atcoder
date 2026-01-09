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

A,B = mi()
A,B = min(A,B), max(A,B)
ans = 0

for i in range(-1000,1000):
    a = min(A,B,i)
    b = max(A,B,i)
    if A < i < B:
        c = i
    elif i < A < B:
        c = A
    elif A < B < i:
        c = B
    else:
        c = i
    if c - a == b - c:
        ans += 1

print(ans)