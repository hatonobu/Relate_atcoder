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
M = ii()
B = li()
L = ii()
C = li()
Q = ii()
X = li()

ans = set()
for a in range(N):
    for b in range(M):
        for c in range(L):
            n = A[a] + B[b] + C[c]
            ans.add(n)

for x in X:
    if x in ans:
        print("Yes")
    else:
        print("No")
