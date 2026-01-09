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

H,W = mi()
S = [input() for _ in range(H)]

lx = INF
hx = -1
ly = INF
hy = -1
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            lx = min(lx,x)
            hx = max(hx,x)
            ly = min(ly,y)
            hy = max(hy,y)

ans = "Yes"
for y in range(ly,hy+1):
    for x in range(lx,hx+1):
        if S[y][x] == ".":
            ans = "No"

print(ans)