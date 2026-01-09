import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue
import math

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

N,M = mi()
AB = lli(M)

cnt = [0] * (N + 1)

for a,b in AB:
    cnt[(a+b)%N] += 1

ans = M * (M - 1) // 2
for i in range(N):
    ans -= cnt[i] * (cnt[i] - 1) // 2

print(ans)