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
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

H,W = mi()
lis = ["s","n","u","k","e"]
S = []
for _ in range(H):
    s = input()
    S.append(s)

check = [[False]*W for _ in range(H)]


count = 0
x = 0
y = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
used = [[False]*W for _ in range(H)]

def dfs(count,x,y,used):
    s = lis[count%5]
    if x == W-1 and y == H-1:
        print("Yes")
        exit()
    for ddx,ddy in zip(dx,dy):
        X = x+ddx
        Y = y+ddy
        if 0 <= X < W and 0 <= Y < H:
            if S[Y][X] == s and used[Y][X] == False:
                used[Y][X] = True
                dfs(count+1,X,Y,used)

if S[y][x] == "s":
    used[0][0] = True
    dfs(1,0,0,used)

print("No")  

