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

T = ii()
ans = []
for _ in range(T):
    a,b,c = mi()
    left = -1
    right = 10**9+1
    while(abs(right - left) > 1):
        mid = (right + left) // 2
        get_max = min(a,c)
        if get_max < mid:
            right = mid
            continue
        cnt = a+b+c - mid*2
        num = min(get_max,cnt)
        if num >= mid:
            left = mid
        else:
            right = mid
    ans.append(left)

print(*ans,sep="\n")