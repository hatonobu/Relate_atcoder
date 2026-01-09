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

N,M = mi()
XY = lli(M)
Q = ii()

V = [[] for _ in range(N+1)]

check = set()

#逆順に着けて、黒くなったら幅優先で頂点を消す
for x,y in XY:
    V[y].append(x)
    
for _ in range(Q):
    v, num = mi()
    if v == 1:
        #幅優先かく
        q = deque()
        if num in check:
            continue
        else:
            check.add(num)
        for now in V[num]:
            q.append(now)
            check.add(now)
        while(q):
            n = q.pop()
            for next in V[n]:
                if next in check:
                    pass
                else:
                    check.add(next)
                    q.append(next)
    else:
        if num in check:
            print("Yes")
        else:
            print("No")