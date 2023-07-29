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
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

S = input()

N = len(S)
dp = [[0]*3005 for _ in range(N+5)]
dp[0][0] = 1

for i,s in enumerate(S):
    for j in range(N):
        if s == "(":
            dp[i+1][j+1] += dp[i][j] % mod
        elif s == ")":
            if j != 0:
                dp[i+1][j-1] += dp[i][j] % mod
        else:
            dp[i+1][j+1] += dp[i][j] % mod
            if j != 0:
                dp[i+1][j-1] += dp[i][j] % mod

print(dp[N][0] % mod)