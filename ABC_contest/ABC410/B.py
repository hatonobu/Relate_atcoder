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

N,Q = mi()
X = li()

B = [0] * (N)

ans = []

for i in range(Q):
    x = X[i]
    if x == 0:
        num = INF
        place = -1
        for i in range(N):
            if B[i] < num:
                num = B[i]
                place = i
        B[place] += 1
        ans.append(place+1)
    else:
        B[x-1] += 1
        ans.append(x)

print(*ans)