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

N,X = mi()
T = li()
#X+1の時のdp[X+1][1]が答え
dp = [defaultdict(set) for _ in range(X+T[0]+2)]
dp[0][0].add(1)

for i in range(X+1):
    for a in dp[i].values():
        for k in a:
            for j in range(N):
                if i + T[j] <= X:
                    dp[i+T[j]][i+T[j]].add(k+1)
                else:
                    if j == 0:
                        dp[i+T[j]][i+T[j]].add(k+1)

print(dp)
ans = 0
for i in range(X+1,X+1+T[0]):
    for a in dp[i].values():
        for k in a:
            num = 1
            for _ in range(k-1):
                num *= N
                num %= mod
            ans += pow(num,-1,mod)
            ans %= mod

print(ans)