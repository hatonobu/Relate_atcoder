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

#https://qiita.com/AkariLuminous/items/a2c789cebdd098dcb503#51-internal_scc
#強連結成分分解：DFSを用いてグループ閉路内で行き来が可能なものにまとめたもの
#add_edge(a,b) : aからbへ行ける経路を追加する
#scc           : 強連結成分を持ったグループを返す(トポロジカルソートされている)
#トポロジカルソート：入力次数の少ない順にソートされたもの。右が多く入力がくる終点。

from atcoder.scc import SCCGraph

N = ii()
A = li()

#強連結成分をまとめたグラフの作成　SCCGraph(n) n: 頂点数
scc_graph = SCCGraph(N)

#各頂点間のグラフ関係を埋める
for i in range(N):
    scc_graph.add_edge(i, A[i]-1)

#グループを取得する
groups = scc_graph.scc()
r = [0] * N
for c in groups[::-1]:
    #閉路を持つとき　or (自己ループを持つとき)
    if len(c) > 1 or (A[c[0]] -1) == c[0]:
        for u in c:
            r[u] = len(c)
    else:
        r[c[0]] = r[A[c[0]] - 1] + 1

print(sum(r))
