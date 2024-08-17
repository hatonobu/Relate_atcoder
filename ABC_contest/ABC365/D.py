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
S = input()

dp = [[-1,-1,-1] for _ in range(N+5)]
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1,N+1):
    num = -1
    s = S[i-1]
    if s == "R":
        num = 0
    elif s == "S":
        num = 1
    else:
        num = 2
    if num == 0:
        dp[i][2] = max(dp[i][2], dp[i-1][1] + 1, dp[i-1][0] + 1)
        dp[i][0] = max(dp[i][0], dp[i-1][1], dp[i-1][2])
    elif num == 1:
        dp[i][0] = max(dp[i][0], dp[i-1][1] + 1, dp[i-1][2] + 1)
        dp[i][1] = max(dp[i][1], dp[i-1][0], dp[i-1][2])
    else:
        dp[i][1] = max(dp[i][1], dp[i-1][2] + 1, dp[i-1][0] + 1)
        dp[i][2] = max(dp[i][2], dp[i-1][1], dp[i-1][0])
    

print(max(dp[:][N]))