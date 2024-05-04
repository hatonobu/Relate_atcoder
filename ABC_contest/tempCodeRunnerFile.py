import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect

sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
lli_st = lambda n: [list(input()) for _ in range(n)]
mod = 998244353
INF = 10**18

H,W = mi()
A = lli_st(H)
q = deque()
q.append([0,0,1,0])
score = [[0]*W for _ in range(H)]
ddx = [1,0]
ddy = [0,1]

ans = -INF
while(q):
    x,y,turn,now_score = q.popleft()
    #print(x,y,turn,now_score)
    if x == W-1 and y == H-1:
        ans = max(ans,now_score)
        continue
    for dx,dy in zip(ddx,ddy):
        nx,ny = x+dx, y+dy
        if 0 <= nx < W and 0 <= ny < H:
            if A[ny][nx] == "-":
                now_score += turn*(-1)
            else:
                now_score += turn
            q.append([nx,ny,turn*-1,now_score])

if ans > 0:
    print("Takahashi")
elif ans == 0:
    print("Drow")
else:
    print("Aoki")    