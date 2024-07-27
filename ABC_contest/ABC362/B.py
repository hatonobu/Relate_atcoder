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

x1,y1 = mi()
x2,y2 = mi()
x3,y3 = mi()
a = (x2-x1)**2 + (y2-y1)**2
b = (x3-x2)**2 + (y3-y2)**2
c = (x1-x3)**2 + (y1-y3)**2

if (a+b == c) or (b+c == a) or (c + a == b):
    print("Yes")
else:
    print("No")



