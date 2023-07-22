import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import copy

sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,M = mi()
S = [list(input()) for _ in range(N)]
used_map = set()
lis = copy.deepcopy(S)
dots = 0
for n in S:
    a = n.count(".")
    dots += a

dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans_dots = dots

def black(x,y,dx,dy):
    while(1):
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= M or y >= N or S[y][x] == "#":
            break
        else:
            lis[y][x] = "#"       
    return x-dx,y-dy       


def dfs(x,y):
    if (x,y) in used_map:
        return
    used_map.add((x,y))
    global ans_dots
    
    for ddx,ddy in zip(dx,dy):
        if S[y+ddy][x+ddx] == ".":
            ax,ay = black(x,y,ddx,ddy)
            dfs(ax,ay)

lis[1][1] = "#"
dfs(1,1)

num = 0
for n in lis:
    a = n.count(".")
    num += a
ans_dots = min(ans_dots,num)

print(dots - ans_dots)
