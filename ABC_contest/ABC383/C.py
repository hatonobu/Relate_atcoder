import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 8 * 10**18

H,W,D = mi()
S = [list(input()) for _ in range(H)]
used_map = [[-INF]*W for _ in range(H)]

q = []
heapq.heapify(q)
for y in range(H):
    for x in range(W):
        if S[y][x] == "H":
            q.append([-D,x,y])
            used_map[y][x] = D
        elif S[y][x] == ".":
            used_map[y][x] = -1
        else:
            pass

while(q):
    ddx = [-1,0,1,0]
    ddy = [0,1,0,-1]
    d,x,y = heapq.heappop(q)
    d *= -1
    if d <= 0:
        pass
    else:
        for dx,dy in zip(ddx,ddy):
            nx,ny = x+dx, y+dy
            if 0 <= nx < W and 0 <= ny < H:
                if used_map[ny][nx] == -1:
                    used_map[ny][nx] = d-1
                    heapq.heappush(q,[-1*(d-1),nx,ny])
                    

ans = 0
for y in range(H):
    for x in range(W):
        if used_map[y][x] >= 0:
            ans += 1
                
print(ans)