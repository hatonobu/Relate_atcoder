import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

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

N,M,K = mi()
left = 0
right = 2*10**18 + 10
k = math.lcm(N,M)

def is_ok(arg):
    num = (mid // N) + (mid // M) - 2 * (mid // k)
    if num >= K:
        return True
    else:
        return False

while (abs(right - left) > 1):
    mid = (right + left) // 2
    if is_ok(mid):
        right = mid
    else:
        left = mid

print(right)