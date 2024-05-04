import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

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

#https://note.nkmk.me/python-union-find/
from collections import deque,defaultdict

class UnionFind():
    #__init__
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    #要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    #要素x,要素yが属するグループを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    #要素xが属するグループのサイズを返す
    def size(self, x):
        return -self.parents[self.find(x)]
    #要素x,yが同じグループに属するか返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
    #要素xが属するグループの要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    #全ての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    #グループの数を返す
    def group_count(self):
        return len(self.roots())
    #ルート要素のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    #printでの表示用
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

lis = [0]*N
uf = UnionFind(N)
for i in range(M):
    a,b = mi()
    a -= 1
    b -= 1
    uf.union(a,b)
    lis[a] += 1
    lis[b] += 1

ans = 0
for n,check in uf.all_group_members().items():
    total = 0
    for l in check:
        total += lis[l]
    ans += len(check) * (len(check) - 1) // 2 - (total // 2)

print(ans)

