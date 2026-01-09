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
    N = ii()
    A = li()
    
    A = sorted(A, key=lambda x: abs(x))
    print(A)
    ans = "Yes"
    for i in range(1,N-1):
        if A[i]**2 != A[i-1] * A[i+1]:
            ans = "No"
            break
    
    print(ans)