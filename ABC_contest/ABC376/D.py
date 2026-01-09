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

N,M = mi()
G = [[] for _ in range(N)]
d = [set() for _ in range(N)]

for i in range(M):
    a,b = mi()
    G[a-1].append([b-1,1])
    d[a-1].add(b-1)
# https://qiita.com/Yuya-Shimizu/items/eefdc6f854534e90c988

import heapq

def dijkstra(edges, num_node,start):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [8*10**18] * num_node    #スタート地点以外の値は∞で初期化
    node[start] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, start])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)
        
        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[min_point] + cost, goal])

    return node

node_num = N

opt_node = dijkstra(G, node_num,0)

ans = INF
for i in range(1,N):
    if 0 in d[i]:
        ans = min(opt_node[i]+1,ans)

print(ans if ans < 10**12 else -1)

