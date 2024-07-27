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
B = li()
A.sort()
B.sort()

a_now = 0
ans = 0
b_now = 0

while(a_now < N and b_now < M):
    if A[a_now] >= B[b_now]:
        ans += A[a_now]
        b_now += 1
    a_now += 1

if b_now != M or (a_now == N and b_now < M):
    ans = -1

print(ans if ans != 0 else -1)
