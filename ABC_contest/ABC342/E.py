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

# https://qiita.com/Yuya-Shimizu/items/eefdc6f854534e90c988

import heapq

def dijkstra(edges, num_node,start):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [-INF] * num_node    #スタート地点以外の値は∞で初期化
    node[start] = -INF     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [-INF, start])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)
        
        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            l,d,k,c  = factor[1]   #コスト

            #更新条件
            #print(l,min(k - 1, (-node[goal] - l - c) // d) * d ,node[goal],min_point)
            if -l > node[goal] + c:
                if -(l + (k-1)*d) >= node[goal] + c:
                    node[goal] = -(l + (k-1)*d)
                else:
                    node[goal] = l + ((-node[goal] - l - c) // d) * d  #更新
                    pass
                print(node,min_point)
                #ヒープに登録
                heapq.heappush(node_name, [node[goal], goal])

    return node

Edges = [[] for _ in range(N)]
for i in range(M):
    l,d,k,c,A,B = mi()
    A -= 1
    B -= 1
    Edges[B].append([A,[l,d,k,c]])

#頂点数
node_num = N

opt_node = dijkstra(Edges, node_num,N-1)

print(opt_node)
