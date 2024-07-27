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

N = ii()
LR = []
check = 0
for i in range(N):
    l,r = mi()
    LR.append([l,r])
    check += l

lis = []
for l,r in LR:
    if check == 0:
        lis.append(l)
    elif check > 0:
        print("No")
        exit()
    else:
        if (r-l) > abs(check):
            lis.append(l+abs(check))
            check = 0
        else:
            lis.append(r)
            check += (r-l)

if check == 0:
    print("Yes")
    print(*lis)
else:
    print("No")