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
li = lambda: list(mi())
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,M = mi()
ans = 1

dp = [[0]*(N+5) for _ in range(2)]

dp[1][1] = M
for i in range(1,N):
    dp[0][i+1] += dp[0][i]*(M-2)
    dp[1][i+1] += dp[0][i]
    dp[0][i+1] += dp[1][i]*(M-1)
    dp[0][i+1] %= mod
    dp[1][i+1] %= mod

print(dp[0][N])