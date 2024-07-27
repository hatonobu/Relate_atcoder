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

N,K = mi()
a = (1 - (2 * (N-1) * pow(N*N,mod-2,mod))) % mod
b = ((1-a) * pow(N-1,mod-2,mod)) % mod
n_a = a
n_b = b

for i in range(1,K):
    n_a = (n_a*a + n_b*b*(N-1)) % mod
    n_b = ((1 - n_a) * pow(N-1,mod-2,mod)) % mod

ans = 0
d = N*(N+1) // 2
d -= 1
ans += n_a
ans += (d*n_b)
print(ans % mod)