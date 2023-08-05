import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

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

dots = 0
for n in S:
    a = n.count(".")
    dots += a

ans_dots = dots

x,y = 1,1
dx = [0,1,0,-1]
dy = [-1,0,1,0]


def black(x,y,dx,dy,lis):
    while(1):
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= M or y >= N or lis[y][x] == "#":
            break
        else:
            lis[y][x] = "#"       
    return lis        


def dfs(x,y,lis):
    print(x,y)
    for ddx,ddy in zip(dx,dy):
        if lis[y+ddy][x+ddy] == ".":
            dfs(x+ddx,y+ddy,black(x,y,ddx,ddy,lis))

    num = 0
    for n in lis:
        a = n.count(".")
        num += a
    ans_dots = min(ans_dots,num)


dfs(x,y,S)
print(dots - ans_dots)
