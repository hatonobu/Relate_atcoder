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
ans = [["."]*N for _ in range(N)]

for i in range(N):
    j = N - i
    if i <= j:
        if i % 2 == 0:
            for k in range(i,j):
                for l in range(i,j):
                    ans[k][l] = "#"
        else:
            for k in range(i,j):
                for l in range(i,j):
                    ans[k][l] = "."

for i in range(N):
    print("".join(ans[i]))