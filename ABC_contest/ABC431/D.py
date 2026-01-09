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
WHB = lli(N)

p = [0]

for i in range(N):
    w,h,b = WHB[i]
    ans = [0] * (len(p)+w)
    for i in range(len(p)):
        ans[i] = max(ans[i], p[i] + b)
        ans[i+w] = max(ans[i], p[i] + h)
    p = ans

print(max(ans[:((len(ans)-1) // 2) + 1]))