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

N,D,P = mi()
F = li()

ans = sum(F)
F.sort(reverse=True)

check = 0
while(1):
    total = 0
    for i in range(check*D,check*D+D):
        if i < N:
            total += F[i]
        else:
            break
    if total > P:
        ans = ans - total + P
    else:
        break
    check += 1

print(ans)