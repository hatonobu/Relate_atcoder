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
    N,M = mi()
    A = li()
    B = li()
    A.sort()
    B.sort()
    front = 0
    back = 1
    pack = 0
    ans = 0
    for i in range(N):
        if A[-back] + B[i] >= M:
            ans += (A[-back] + B[i]) % M
            back += 1
        else:
            ans += A[front] + B[i]
            front += 1
    print(ans)        