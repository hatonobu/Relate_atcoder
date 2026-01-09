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
H = li()

dp = [[0]*(N+5) for _ in range(3005)]

for i in range(1,N+1):
    num = H[i-1]
    for j in range(1,3000):
        if i-j > 0:
            if H[i-j-1] == num:
                dp[j][i] = dp[j][i-j] + 1
            else:
                dp[j][i] = 1
        else:
            dp[j][i] = 1

ans = -1
for i in range(3001):
    for j in range(N+1):
        ans = max(ans,dp[i][j])

print(ans)