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

N,M = mi()
lis = []

while(M > 0):
    if M % 2 == 1:
        lis.append(1)
    else:
        lis.append(0)
    M //= 2

while(len(lis) < 60):
    lis.append(0)

ans = 0
for i in range(60):
    if lis[i] == 1:
        ans += (N // 2**(i+1)) * 2**i
        ans += max(0,(N % 2**(i+1)) - ((2**i)-1))
        ans %= mod
    #print(ans)

print(ans % mod)
