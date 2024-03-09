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

# https://qiita.com/takayg1/items/c811bd07c21923d7ec69

#list型で引き渡すことに注意
#dp等で使いたい場合は初期リストを生成する : lis = [0]*(N)

#####segfunc#####
def segfunc(x, y):
    if x[0] == y[0]:
        if x[2] == y[2]:
            return ([x[0],y[1]+x[1],x[2],x[3]+y[3]])
        else:
            if x[2] > y[2]:
                return ([x[0],y[1]+x[1],x[2],x[3]])
            else:
                return ([x[0],y[1]+x[1],y[2],y[3]])
    else:
        if x[0] > y[0]:
            if x[2] > y[0]:
                return ([x[0],x[1],x[2],x[3]])
            elif x[2] == y[0]:
                return ([x[0],x[1],x[2],x[3]+y[1]])
            else:
                return ([x[0],x[1],y[0],y[1]])
        else:
            if y[2] > x[0]:
                return ([y[0],y[1],y[2],y[3]])
            elif y[2] == x[0]:
                return ([y[0],y[1],y[2],y[3]+x[1]])
            else:
                return ([y[0],y[1],x[0],x[1]])

#################

#####ide_ele#####
#ide_ele = -float("inf") #最大値
#ide_ele = float("inf") #最小値
#ide_ele = 0 #区緩和等
#ide_ele = 1 #区間積
ide_ele = [0,0,0,0]
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N) 
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
    
    def __getitem__(self, i):
        """[i] で i 番目の値を得られる。O(log n)"""
        if i < 0:
            i %= self.size
        return self.prod(i, i + 1)

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る (開区開であることに注意、rを+1して考える必要がある場合あり)
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

N,Q = mi()
A = li()
B = []
for a in A:
    B.append([a,1,0,0])

seg = SegTree(B, segfunc, ide_ele)
for i in range(Q):
    x,y,z = mi()
    y -= 1
    if x == 1:
        seg.update(y,[z,1,0,0])
    else:
        print(seg.query(y,z)[-1])
