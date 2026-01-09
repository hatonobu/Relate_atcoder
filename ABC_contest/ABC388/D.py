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

N = ii()
A = li()

lis = []
heapq.heapify(lis)

ans = []
for i in range(N):
    while(len(lis) > 0):
        now = heapq.heappop(lis)
        if now - i < 0:
            pass
        else:
            heapq.heappush(lis,now)
            break
    num = max(A[i]+len(lis),0)
    ans.append(max(A[i]-(N-i-1)+len(lis),0))
    heapq.heappush(lis, num+i)
    
print(*ans)
    
        