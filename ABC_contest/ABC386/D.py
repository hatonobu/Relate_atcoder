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
XY_B = []
XY_W = []
for i in range(M):
    X,Y,C = ml()
    X = int(X)
    Y = int(Y)
    if C == "B":
        XY_B.append((X,Y))
    else:
        XY_W.append((X,Y))

XY_B.sort()
XY_newlist = []

for x,y in XY_B:
    while(len(XY_newlist) > 0):
        px,py = XY_newlist.pop()
        if py > y:
            XY_newlist.append((px,py))
            break
        else:
            pass
    XY_newlist.append((x,y))
    
X_list = []
Y_list = []

for x,y in XY_newlist:
    X_list.append(x)
    Y_list.append(y)

ans = "Yes"
for x,y in XY_W:
    idx = bisect.bisect_left(X_list, x)
    if idx >= len(X_list):
        pass
    else:
        if Y_list[idx] >= y:
            ans = "No"

print(ans)