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
H = li()

T = 1
for h in H:
    total = 0
    if T % 3 == 0:
        h -= 3
        total = 1
        if h <= 0:
            T += 1
            continue
    elif T % 3 == 1:
        pass
    else:
        h -= 1
        if h <= 0:
            T += 1
            continue
        h -= 3
        if h <= 0:
            T += 2
            continue
        total = 2

    check = h // 5
    check2 = h % 5
    if check2 == 0:
        total += 0
    elif check2 == 1:
        total += 1
    elif check2 == 2:
        total += 2
    else:
        total += 3
    T += total + check*3

print(T-1)
