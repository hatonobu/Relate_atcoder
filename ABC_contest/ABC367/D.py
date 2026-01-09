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
A = li()
P = [0]*M

ruiseki = [0]
for a in A:
    ruiseki.append(ruiseki[-1] + a)

for a in A[:-1]:
    ruiseki.append(ruiseki[-1] + a)

ans = 0
for i in range(N):
    ans += P[ruiseki[i] % M]
    P[ruiseki[i] % M] += 1

for i in range(N,2*N):
    P[ruiseki[i-N] % M] -= 1
    ans += P[ruiseki[i] % M]

print(ans)