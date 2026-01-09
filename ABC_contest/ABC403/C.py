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

N,M,Q = mi()
ans = []
d = defaultdict(set)
for _ in range(Q):
    lis = li()
    if lis[0] == 1:
        X = lis[1]
        Y = lis[2]
        d[X].add(Y)
    elif lis[0] == 2:
        X = lis[1]
        d[X].add(-1)
    else:
        X = lis[1]
        Y = lis[2]
        if Y in d[X] or -1 in d[X]:
            ans.append("Yes")
        else:
            ans.append("No")
    
print("\n".join(ans))