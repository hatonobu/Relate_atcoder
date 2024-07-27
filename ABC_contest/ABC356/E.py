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
A = li()

#数値の数の累積和
cnt = [0]*(10**6+5)
for a in A:
    cnt[a] += 1

for i in range(10**6+2):
    cnt[i+1] += cnt[i]

#発見した数値をcとする
ans = 0
for c in range(1,10**6+1):
    num = cnt[c] - cnt[c-1] #数値cの個数取得
    #cの幅で見ることでガウス整数の間隔で足せる(logn　になる)
    for window in range(c,10**6+1,c):
        gausu = window // c
        ans += gausu * (cnt[min(10**6,c+window-1)] - cnt[window - 1]) * num
        #num >= 2のときnC2個にしたいのでn^2 - nC2を取る
    ans -= num**2 - (num * (num-1) // 2)

print(ans)


