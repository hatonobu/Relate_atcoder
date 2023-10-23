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

N,A,B,C = mi()
D = lli(N)

import heapq

def dijkstra(edges, num_node,start):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [6*10**18] * num_node    #スタート地点以外の値は∞で初期化
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

Edges = []
Edges_train = []
for i in range(N):
    check = []
    check_train = []
    for j in range(N):
        dist = D[i][j]*A
        check.append([j,dist])
        check_train.append([j,D[i][j]*B + C])
    Edges.append(check)
    Edges_train.append(check_train)

node_num = N

opt_node = dijkstra(Edges, node_num,0)

opt_node_train = dijkstra(Edges_train,node_num,N-1)

ans = 6* 10 ** 18
for i in range(N):
    ans = min(ans,opt_node[i] + opt_node_train[i])

print(ans)