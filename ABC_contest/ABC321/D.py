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
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,M,P = mi()
A = li()
B = li()

B.sort()
l = len(B)
r_b = [0]
for b in B:
    r_b.append(r_b[-1] + b)

ans = 0
for a in A:
    if a > P:
        ans += P * l
        continue
    num = P - a
    p = bisect.bisect_left(B,num)
    ans += P * (l-p)
    ans += a * p + r_b[p]

print(ans)