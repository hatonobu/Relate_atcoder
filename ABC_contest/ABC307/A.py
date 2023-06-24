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
li = lambda: list(mi())
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
A = li()

lis = []
for i in range(N):
    ans = 0
    for j in range(7):
        ans += A[7*i + j]
    lis.append(ans)

print(*lis)
