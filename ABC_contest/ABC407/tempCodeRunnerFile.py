import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10 ** 9)
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
A = lli(H)
for i in range(H):
    A[i].append(0)
A.append([0] * (W + 1))

total = 0
for i in range(H):
    for j in range(W):
        total ^= A[i][j]

ans = 0
check = 0
B = [[False] * (W + 1) for _ in range(H + 1)]

def dfs(x, y):
    global check
    global ans
    ans = max(ans, total ^ check)
    if y == H:
        return True
    if B[y][x] == False and B[y][x + 1] == False:
        B[y][x] = True
        B[y][x + 1] = True
        check ^= A[y][x] ^ A[y][x + 1]
        if x+1 < W:
            dfs(x + 1, y)
        else:
            dfs(0, y + 1)
        B[y][x] = False
        B[y][x + 1] = False
        check ^= A[y][x] ^ A[y][x + 1]
    if B[y][x] == False and B[y + 1][x] == False:
        B[y][x] = True
        B[y + 1][x] = True
        check ^= A[y][x] ^ A[y + 1][x]
        if x+1 < W:
            dfs(x + 1, y)
        else:
            dfs(0, y + 1)
        B[y][x] = False
        B[y + 1][x] = False
        check ^= A[y][x] ^ A[y + 1][x]
    if x+1 < W:
        dfs(x + 1, y)
    else:
        dfs(0, y + 1)
    
dfs(0, 0)
print(ans)
        