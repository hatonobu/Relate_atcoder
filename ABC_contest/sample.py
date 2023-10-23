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

l = 0
now = X

for i in range(1,N*X*2):
    l += 1
    dp[i] = dp[i-1] + now
    now -= F
    if now <= 0:
        break

times = (N-dp[l]) // S
for i in range(1,times+1):
    now = S
    
    
