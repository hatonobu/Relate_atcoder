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

sx,sy = mi()
tx,ty = mi()
ans = abs(ty - sy)
total_x = abs(sx-tx)
total = abs(ty - sy) - 1
check = 0
#目標が左
if tx < sx :
    if sy % 2 == 0:
        if sx % 2 == 0:
            pass
        else:
            total += 1
    else:
        if sx % 2 == 0:
            total += 1
        else:
            pass
    check = max(0,abs(sx-tx) - total) // 2

    if ty % 2 == 0:
        pass
    else:
        pass
elif tx == sx:
    check = 0
#目標が右
else:
    if sy % 2 == 0:
        if sx % 2 == 0:
            total += 1
        else:
            pass
    else:
        if sx % 2 == 0:
            pass
        else:
            total += 1
    check = max(0,abs(sx-tx) - total) // 2

print(ans + check)