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

ans = 0
total = 0
if N-K < K:
    num = 0
    for i in A:
        num ^= i
    for e in itertools.combinations(A,N-K):
        check = num
        for n in e:
            check ^= n
        ans = max(ans,check)
else:
    for e in itertools.combinations(A,K):
        num = 0
        for n in e:
            total += 1
            num ^= n
        ans = max(ans,num)

print(ans)