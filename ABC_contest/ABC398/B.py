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

A = li()
lis = [0]*20
for i in A:
    lis[i] += 1

check2 = False
check3 = False
check4 = False
for i in range(14):
    if lis[i] == 2:
        check2 = True
    if lis[i] >= 3:
        if check3:
            check4 = True
        else:
            check3 = True

if (check2 and check3) or check4:
    print("Yes")
else:
    print("No")