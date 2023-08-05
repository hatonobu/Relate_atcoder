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

dp = [[0]*3000 for _ in range(3000)]
dp[0] = 1
print(dp)
num = 0
for i,s in enumerate(1,S):
    if s == "(":
        num += 1
        dp[i+1][num] = dp[i][num-1]
    elif s == ")":
        num = max(num-1,0)
        dp[i+1][num] = dp[i][num+1]