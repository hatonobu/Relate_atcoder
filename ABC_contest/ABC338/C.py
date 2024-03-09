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

Q = li()
A = li()
B = li()
ans = INF
for i in range(N):
    if B[i] != 0:
        ans = min(ans,Q[i] // B[i])

check = True
for i in range(1,10**6+5):
    k = INF
    for j in range(N):
        Q[j] -= A[j]
        if Q[j] < 0:
            check = False
            break
        if B[j] != 0:
            k = min(k,Q[j] // B[j])
    if check == False:
        break
    if 0 <= k < INF:
        ans = max(ans,k + i)

print(ans)