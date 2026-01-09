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

N,X = mi()
APBQ = lli(N)
left = -1
right = 10**10

while(abs(right - left) > 1):
    total = X
    mid = (right + left) // 2
    for i in range(N):
        a,p,b,q = APBQ[i]
        cost = INF
        for j in range(100):
            if (mid-a*j) < 0:
                break
            cost = min(cost, j*p + ((((mid-a*j - 1) // b) + 1 )*q))
        for j in range(100):
            if (mid-b*j) < 0:
                break
            cost = min(cost, j*q + ((((mid-b*j - 1) // a) + 1 )*p))
        total -= cost 
    if total < 0:
        right = mid
    else:
        left = mid

print(left)
        
    
