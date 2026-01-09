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
    
for _ in range(T):
    N,H = mi()
    p_left = H
    p_right = H
    now = 0
    ans = "Yes"
    for i in range(N):
        t,l,u = mi()
        delta = t - now
        
        now = t
        left = p_left - delta
        right = p_right + delta
        
        p_left = max(left, l)
        p_right = min(right, u)
        
        if p_left > p_right:
            ans = "No"
        else:
            pass
    print(ans)