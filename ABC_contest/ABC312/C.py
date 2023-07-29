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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
 
N,M = mi()
A = li()
B = li()
 
A.sort()
B.sort()

ans = B[-1]+1
 
for i in range(N):
    num = M - bisect.bisect_left(B,A[i])
    if num <= i+1:
        print(min(ans,A[i]))
        exit()
    else:
        if i+2 < M:
            ans = min(ans,B[-(i+2)]+1)
 
print(ans)