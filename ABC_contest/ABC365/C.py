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
ruiseki = [0]

A.sort()

for a in A:
    ruiseki.append(ruiseki[-1] + a)

if ruiseki[-1] <= M:
  print("infinite")
  exit()

left = -1
right = M + 100
while(abs(right - left) > 1):
    mid = (right + left) // 2
    idx = bisect.bisect_left(A,mid)
    total = ruiseki[idx] + mid*(N-idx)
    if total <= M:
       left = mid
    else:
       right = mid

print(left)