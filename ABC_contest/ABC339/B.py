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

H,W,N = mi()
check = [list("."*W) for _ in range(H)]
x = 0
y = 0
n = 0
for i in range(N):
    if check[y][x] == ".":
        n += 1
        check[y][x] = "#"
    else:
        n -= 1
        check[y][x] = "."
    n = n % 4
    if n == 0:
        y -= 1
    elif n == 1:
        x += 1
    elif n == 2:
        y += 1
    else:
        x -= 1
    if y == -1:
        y = H-1
    if y == H:
        y = 0
    if x == -1:
        x = W-1
    if x == W:
        x = 0

for c in check:
    print("".join(c))

