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
S = li_st()

dp = [[0]*(26) for _ in range(2*10**5+1)]

for s in S:
    for i in range(len(s)):
        num = ord(s[i]) - ord("a")
        dp[i][num] += 1

ans = 0
for k in range(N-1):
    s = S[k]

    for i in range(len(s)):
        num = ord(s[i]) - ord("a")
        if dp[i][num] > 1:
            ans += (dp[i][num] - 1)
        else:
            break

    for j in range(len(s)):
        num = ord(s[j]) - ord("a")
        dp[j][num] -= 1

print(ans)