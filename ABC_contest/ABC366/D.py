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

for x in range(N):
    for y in range(N):
        n = li()
        for z in range(N):
            N_matrix[x][y][z] = n[z]

def cumulative_sum_3d(matrix):
    # 元の行列のサイズを取得
    depth = len(matrix)
    rows = len(matrix[0])
    cols = len(matrix[0][0])
    
    # 初めに0で満たされた累積和を格納するための行列を作成
    cum_sum = [[[0] * (cols + 1) for _ in range(rows + 1)] for _ in range(depth + 1)]
    
    # 累積和を計算
    for k in range(1, depth + 1):
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                cum_sum[k][i][j] = (matrix[k-1][i-1][j-1] +
                                    cum_sum[k-1][i][j] +
                                    cum_sum[k][i-1][j] +
                                    cum_sum[k][i][j-1] -
                                    cum_sum[k-1][i-1][j] -
                                    cum_sum[k-1][i][j-1] -
                                    cum_sum[k][i-1][j-1] +
                                    cum_sum[k-1][i-1][j-1])
    
    return cum_sum

ruisekiMatrix = cumulative_sum_3d(N_matrix)


Q = ii()
for i in range(Q):
    x1,x2,y1,y2,z1,z2 = mi()
    x1 -= 1
    y1 -= 1
    z1 -= 1
    ans = (ruisekiMatrix[x2][y2][z2]
    - ruisekiMatrix[x1][y2][z2]
    - ruisekiMatrix[x2][y1][z2]
    - ruisekiMatrix[x2][y2][z1]
    + ruisekiMatrix[x1][y1][z2]
    + ruisekiMatrix[x1][y2][z1]
    + ruisekiMatrix[x2][y1][z1]
    - ruisekiMatrix[x1][y1][z1])
    print(ans)
