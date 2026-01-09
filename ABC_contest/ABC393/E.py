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
A = li()
M = 10**6 + 5

C = [0]*M
ans = [0]*M

for a in A:
    C[a] += 1

for i in range(1,M):
    total = 0
    for j in range(i,M,i):
        total += C[j]
    if total >= K:
        for k in range(i,M,i):
            ans[k] = i

for a in A:
    print(ans[a])
    
                