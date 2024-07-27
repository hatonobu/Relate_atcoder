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
A = [0] * N
B = [0] * N
for i in range(N):
    A[i],B[i] = mi()

dp = [False] * (2**N)
#maskが場の状況。1がおいている0がない状態
for mask in range(2**N):
    for i in range(N):
        for j in range(i+1,N):
            #mask ^ (1 << i) ^ (a << j)では、maskの場の状況からiとjを追加する前の状況と比べる。
            if (mask >> i & 1) and (mask >> j & 1) and (A[i] == A[j] or B[i] == B[j]) and dp[mask ^ (1<<i) ^ (1<<j)] == False:
                dp[mask] = True
                                                        

print("Takahashi" if dp[2**N-1] else "Aoki")