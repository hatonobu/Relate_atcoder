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

    
N,K = mi()
P = li()
check =  [-1]*(N)
for i in range(N):
    num = P[i]
    check[num-1] = i

# https://qiita.com/takayg1/items/c811bd07c21923d7ec69

#list型で引き渡すことに注意
#dp等で使いたい場合は初期リストを生成する : lis = [0]*(N)

#####segfunc#####
def segfunc1(x, y):
    return max(x,y)
    #return min(x,y)
    #return (x+y)
    #return (x*y)
    #return gcd(x,y)
#################
def segfunc2(x, y):
    return min(x,y)

#####ide_ele#####
ide_ele1 = -float("inf") #最大値
ide_ele2 = float("inf") #最小値
#ide_ele = 0 #区緩和等
#ide_ele = 1 #区間積
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

seg = SegTree(check, segfunc1, ide_ele1)
seg2 = SegTree(check,segfunc2,ide_ele2)
ans = INF
for i in range(N-K+1):
    ans = min(ans,seg.query(i,i+K) - seg2.query(i,i+K))

print(ans)
