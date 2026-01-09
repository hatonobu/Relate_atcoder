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
A = [input() for _ in range(H)]
check_omote = [[-1]*W for _ in range(H)]
check_ura = [[-1]*W for _ in range(H)]

sx,sy = -1,-1
gx,gy = -1,-1
isWall = True
for y in range(H):
    for x in range(W):
        if A[y][x] == "S":
            sx,sy = x,y
        if A[y][x] == "G":
            gx,gy = x,y
        

dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()
q.append((sx,sy,1,0)) #x,y,第三引数,距離

#幅優先探索、第三引数で表世界と裏世界を管理
check_omote[sy][sx] = 0

while q:
    x,y,z,d = q.popleft()
    if z == 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < W and 0 <= ny < H:
                if A[ny][nx] != "#" and check_omote[ny][nx] == -1 and A[ny][nx] != "x":
                    check_omote[ny][nx] = d + 1
                    if A[ny][nx] == "?":
                        q.append((nx,ny,-1,d+1))
                    else:
                        q.append((nx,ny,1,d+1))
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < W and 0 <= ny < H:
                if A[ny][nx] != "#" and check_ura[ny][nx] == -1 and A[ny][nx] != "o":
                    check_ura[ny][nx] = d + 1
                    if A[ny][nx] == "?":
                        q.append((nx,ny,1,d+1))
                    else:
                        q.append((nx,ny,-1,d+1))

if check_omote[gy][gx] == -1 and check_ura[gy][gx] == -1:
    print(-1)
elif check_omote[gy][gx] == -1:
    print(check_ura[gy][gx])
elif check_ura[gy][gx] == -1:
    print(check_omote[gy][gx])
else:
    print(min(check_omote[gy][gx],check_ura[gy][gx]))
    
