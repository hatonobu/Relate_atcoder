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

T,M = mi()
kaijou_list = []
for i in range(1, 3*10**5+1):
    if i == 1:
        kaijou_list.append(1)
    else:
        kaijou_list.append((kaijou_list[-1]*i)%mod)

for _ in range(T):
    N = ii()
    C = li()
    