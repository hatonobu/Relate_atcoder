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
INF = 8 * 10**18

X = ii()
N = ii()
W = li()
Q = ii()

check = [False]*N

ans = X
for _ in range(Q):
    P = ii()
    P -= 1
    if check[P]:
       ans -= W[P]
       check[P] = False
    else:
        ans += W[P]
        check[P] = True
    
    print(ans)