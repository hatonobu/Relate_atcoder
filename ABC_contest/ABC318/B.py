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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
S = [[False]*105 for _ in range(105)]

for i in range(N):
    a,b,c,d = mi()
    for x in range(a,b):
        for y in range(c,d):
            S[y][x] = True

ans = 0
for i in range(101):
    for j in range(101):
        if S[i][j] == True:
            ans += 1

print(ans)