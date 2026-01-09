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

N,K = mi()
ABC = lli(N)

lis = []
now = 0
now_time = 0
heapq.heapify(lis)
ans = []

for i in range(N):
    a,b,c = ABC[i]
    if now + c <= K:
        now += c
        now_time = max(now_time,a)
        heapq.heappush(lis,(now_time+b,c))
        ans.append(now_time) 
    else:
        now_time = max(now_time,a)
        while(now + c > K):
            n = heapq.heappop(lis)
            now -= n[1]
            now_time = max(now_time,n[0])
        heapq.heappush(lis,(now_time+b,c))
        now += c
        ans.append(now_time)

print(*ans,sep="\n")