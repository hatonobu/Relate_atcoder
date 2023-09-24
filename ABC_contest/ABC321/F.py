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

Q,K = mi()
dp = [0]*5005
dp[0] = 1
ans = []

for i in range(Q):
    s,num = ml()
    num = int(num)
    if s == "+":
        for i in range(K,num-1,-1):
            dp[i] += dp[i-num]
            dp[i] %= mod
    else:
        for i in range(num, K+1):
            dp[i] -= dp[i-num]
            dp[i] %= mod

    ans.append(dp[K])

print(*ans,sep="\n")

