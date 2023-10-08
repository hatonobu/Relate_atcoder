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

dp = [0 for _ in range(X+2)]

for i in range(X+1):
    for j in range(N):
        if T[j] > i:
            if j == 0:
                dp[i] += 1
        else:
            dp[i] += dp[i - T[j]]
    dp[i] = (dp[i] * pow(N,-1,mod)) % mod

print(dp[X])