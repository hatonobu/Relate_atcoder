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
INF = 10**18

H,W = mi()
A = lli(H)
B = lli(H)

ans = INF
for p in itertools.permutations(range(H)):
    for q in itertools.permutations(range(W)):
        match = True
        for i in range(H):
            for j in range(W):
                if A[p[i]][q[j]] != B[i][j]:
                    match = False
        if not match:
            continue

        ans1,ans2 = 0,0
        for i in range(H):
            for j in range(H):
                if i < j and p[i] > p[j]:
                    ans1 += 1
        for i in range(W):
            for j in range(W):
                if i < j and q[i] > q[j]:
                    ans2 += 1
        
        ans = min(ans,ans1+ans2)

print(ans if ans != INF else -1)
    
