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

for i in range(ii()):
    N,K = mi()
    A = li()
    B = li()
    C = [(a,b) for a,b in zip(A,B)]
    C.sort()
    
    ans = INF
    lis = []
    heapq.heapify(lis)
    total = 0
    for i in range(N):
        a,b = C[i]
        if len(lis) == K-1:
            ans = min(ans,a*(b+total))
        heapq.heappush(lis,-b)
        total += b
        if len(lis) == K:
            total -= -heapq.heappop(lis)
            
    print(ans)
        
