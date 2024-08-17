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
INF = 8 * 10**18

N = ii()
N_matrix = [[[0]*N for _ in range(N)] for _ in range(N)]
X_ruiseki = []
Y_ruiseki = []
Z_ruiseki = []
ruisekiMatrix = [[[0]*(N+3) for _ in range(N+3)] for _ in range(N+3)]

for x in range(N):
    for y in range(N):
        n = li()
        for z in range(N):
            N_matrix[x][y][z] = n[z]

for x in range(1,N+1):
    for y in range(1,N+1):
        for z in range(1,N+1):
            ruisekiMatrix[x][y][z] = ruisekiMatrix[x][y-1][z] + ruisekiMatrix[x][y][z-1] - ruisekiMatrix[x][y-1][z-1] + N_matrix[x-1][y-1][z-1]


Q = ii()
for i in range(Q):
    x1,x2,y1,y2,z1,z2 = mi()
    y1 -= 1
    z1 -= 1
    ans = 0
    for i in range(x1,x2+1):
        ans += ruisekiMatrix[i][y2][z2] - ruisekiMatrix[i][y1][z2] - ruisekiMatrix[i][y2][z1] + ruisekiMatrix[i][y1][z1]
        print(ruisekiMatrix[i][y2][z2], ruisekiMatrix[i][y1][z2], ruisekiMatrix[i][y2][z2], ruisekiMatrix[i][y1][z1])
    print(ans)
