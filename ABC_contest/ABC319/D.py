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

N,M = mi()
L = li()

num = sum(L)
left = max(L)-1
right = 10**18

while(abs(left-right)>1):
    times = 1
    mid = (left + right) // 2
    total = -1
    for n in L:
        total += n + 1
        if total > mid:
            times += 1
            total = n

    if times > M:
        left = mid
    else:
        right = mid

print(right)
