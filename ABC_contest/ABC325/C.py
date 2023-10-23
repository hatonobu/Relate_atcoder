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

H,W = mi()
S = [input() for _ in range(H)]
check = [[0]*(W) for _ in range(H)]

def print_lis(lis):
    for i in lis:
        print(i)
    print("==================")

ans = 0
def char(x,y,ans):
    ddx = [1,1,1,0,-1,-1,-1,0]
    ddy = [-1,0,1,1,1,0,-1,-1]
    q = deque()
    q.append([x,y])
    while(q):
        sxx,syy = q.popleft()
        for dx,dy in zip(ddx,ddy):
            sx = sxx + dx
            sy = syy + dy
            if 0 <= sx < W and 0 <= sy < H:
                if S[sy][sx] == "#" and check[sy][sx] == 0:
                    q.append([sx,sy])
                check[sy][sx] = ans


for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            if check[y][x] == 0:
                ans += 1
            char(x,y,ans)

print(ans)
