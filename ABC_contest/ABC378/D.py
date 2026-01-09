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

H,W,K = mi()
S = [list(input()) for _ in range(H)]

ddx = [-1,0,1,0]
ddy = [0,1,0,-1]
ans = 0

def dfs(sx,sy,used,num):
    global ans
    if num == K:
        ans += 1
        return 
    else:
        for dx,dy in zip(ddx,ddy):
            nx = sx + dx
            ny = sy + dy
            if 0 <= nx < W and 0 <= ny < H:
                if used[ny][nx] == True:
                    pass
                else:
                    if S[ny][nx] == ".":
                        used[ny][nx] = True
                        dfs(nx,ny,used,num+1)
                        used[ny][nx] = False

used = [[False]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            used[y][x] = True
            dfs(x,y,used,0)
            used[y][x] = False

print(ans)