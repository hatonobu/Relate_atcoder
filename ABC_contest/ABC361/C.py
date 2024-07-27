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
if N-K == 1:
    print(0)
    exit()
q = deque()
A = li()
A.sort()
check = []
for i in range(N-1):
    check.append(A[i+1] - A[i])

ans = INF

total = 0
c = 0
t = 0
for i in range(N-1):
    c += check[i]
    total += 1
    if total >= N-K-1:
        ans = min(ans,c)
        c -= check[t]
        t += 1
        total -= 1

print(ans)