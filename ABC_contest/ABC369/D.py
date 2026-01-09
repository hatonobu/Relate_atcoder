import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
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

N = ii()
A = li()

dp = [[0,0] for _ in range(N+3)]

for i in range(N):
    if dp[i][1] > 0:
        dp[i+1][0] = max(dp[i][0], dp[i][1] + A[i]*2)
    else:
        dp[i+1][0] = dp[i][0]
    dp[i+1][1] = max(dp[i][1], dp[i][0] + A[i])

print(max(dp[N]))