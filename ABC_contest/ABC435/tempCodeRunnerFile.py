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
A = li()

ans = 0
for l in range(N):
    for r in range(l,N):
        num = sum(A[l:r+1])
        check = True
        for n in range(r):
            if num % A[n] == 0:
                check = False
        if check:
            ans += 1

print(ans)