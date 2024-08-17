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
a = li()
a.sort()

ans = []
for _ in range(Q):
    b,k = mi()
    left = -1
    right = 2* 10**8 + 5
    while(abs(left - right) > 1):
        mid = (right + left) // 2
        l = bisect.bisect_left(a,b-mid)
        r = bisect.bisect_right(a,b+mid)
        if r - l >= k:
            right = mid
        else:
            left = mid
    
    ans.append(right)

print(*ans,sep="\n")