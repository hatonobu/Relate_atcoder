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

N,M = mi()
UVT = lli(M)
#https://pydocument.hatenablog.com/entry/2023/04/27/001232

#graphの指定は以下のような形式
#graph = [[0, 5, INF, 10],
#         [INF, 0, 3, INF],
#         [INF, INF, 0, 1],
#         [INF, INF, INF, 0]]
INF = 10**18

def floyd_warshall(graph):
    n = len(graph)
    dist = [[INF for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = [[INF]*(N+2) for _ in range(N+2)]
for i in range(M):
    u,v,t = UVT[i]
    graph[u][v] = min(graph[u][v],t)
    graph[v][u] = min(graph[v][u],t)
g = floyd_warshall(graph)

for i in range(1,N+1):
    g[i][i] = 0

Q = ii()
for i in range(Q):
    K = ii()
    B = li()
    ans = INF
    for e in itertools.permutations(B):
        for e2 in itertools.product(range(2),repeat=K):
            total = 0
            now = 1
            for i in range(K):
                u,v,t = UVT[e[i]-1]
                if e2[i] == 0:
                    total += g[now][u]
                    now = v
                else:
                    total += g[now][v]
                    now = u
                total += t
            total += g[now][N]
            ans = min(ans,total)
    print(ans)