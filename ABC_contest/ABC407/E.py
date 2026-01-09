import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10 ** 9)
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
for _ in range(T):
    N = ii()
    ans = 0
    lis = []
    heapq.heapify(lis)
    for i in range(2*N):
        if i == 0:
            ans += ii()
        elif i == 2*N - 1:
            num = ii()
        else:
            num = ii()
            heapq.heappush(lis, num * -1)
            if i % 2 == 0:
                ans += -1 * heapq.heappop(lis)
    print(ans)