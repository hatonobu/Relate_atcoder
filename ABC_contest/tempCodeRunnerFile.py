import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,X,F,S = mi()
dp = [0] * (100000)
life = [-1] * (100000)
life[0] = X

#前から来たらlife[num-1] - F
#休憩後から来たらlife[kyuukei] - F
for i in range(1,N*X):
    if dp[i-1] + life[i-1] - F > dp[i]:
        life[i] = max(0,life[i-1] - F)
        dp[i] = dp[i-1] + life[i-1]
    life[i+3] = min(X-F, life[i]+S)
    dp[i+4] = dp[i] + min(X,life[i]+S)

    if dp[i] >= N:
        print(i)
        print(life[:10])
        print(dp[:10])
        exit()

