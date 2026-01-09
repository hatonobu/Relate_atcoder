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

ans = 0
for i in range(1,61):
    a = 2**i
    if a > N:
        break    
    left = -1
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        if mid**2 * a <= N:
            left = mid
        else:
            right = mid

    ans += (left + 1) // 2

print(ans)