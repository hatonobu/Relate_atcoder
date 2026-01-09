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

for i in range(T):
    N = ii()
    A = li()
    ans = set()
    A.append(INF)
    d = defaultdict(list)
    for i in range(2*N):
        if A[i] != A[i+1]:
            d[A[i]].append(i)
    ignore_set = set()
    for i in range(N):
        if len(d[i+1]) != 2:
            ignore_set.add(i+1)
    for i in range(2*N-1):
        a = A[i]
        b = A[i+1]
        if a not in ignore_set and b not in ignore_set:
            lis = [d[a][0], d[a][1], d[b][0], d[b][1]]
            lis.sort()
            if lis[0] + 1 == lis[1] and lis[2] + 1 == lis[3]:
                ans.add((min(a,b), max(a,b)))
            
    print(len(ans))