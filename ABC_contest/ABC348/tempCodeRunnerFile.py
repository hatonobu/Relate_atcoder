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
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 8 * 10**18

H,W = mi()
A = [list(input()) for _ in range(H)]
N = ii()
d = defaultdict(int)
for _ in range(N):
    R,C,E = mi()
    d[(R-1,C-1)] = E

for y in range(H):
    for x in range(W):
        if A[y][x] == "S":
            sy,sx = y,x
        elif A[y][x] == "T":
            gy,gx  = y,x 

if d[(sy,sx)]:
    hp = d[(sy,sx)]
else:
    print("No")
    exit()

ddy = [1,0,-1,0]
ddx = [0,1,0,-1]
A[sy][sx] = hp

q = deque()
q.append((sy,sx))

while(q):
    print(A)
    sy,sx = q.popleft()
    hp = A[sy][sx]
    if d[(sy,sx)]:
        hp = max(hp,d[(sy,sx)])
    if hp == 0:
        continue
    for dx,dy in zip(ddx,ddy):
        nx,ny = sx+dx, sy+dy
        if (0 <= ny < H and 0 <= nx < W):
            if A[ny][nx] == ".":
                A[ny][nx] = hp-1
                q.append((ny,nx))
            elif A[ny][nx] == "S":
                pass
            elif A[ny][nx] == "T":
                print("Yes")
                exit()
            elif A[ny][nx] == "#":
                pass
            else:
                if int(A[ny][nx]) < hp-1:
                    A[ny][nx] = hp-1
                    q.append((ny,nx))

print("No")

