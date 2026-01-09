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
B = li()
W = li()

B.sort(reverse=True)
W.sort(reverse=True)

ans = 0
total_B = 0
total_W = 0
for i in range(N):
    if B[i] > 0:
        ans += B[i]
        total_B += 1

for j in range(M):
    if W[j] > 0:
        ans += W[j]
        total_W += 1

if total_B >= total_W:
    print(ans)
else:
    check = total_W - total_B
    for i in range(total_W-1,total_B-1,-1):
        if 0 <= i < N:
            if B[i] + W[i] > 0:
                ans += B[i]
            else:
                ans -= W[i]
        else:
            ans -= W[i]
    print(ans)