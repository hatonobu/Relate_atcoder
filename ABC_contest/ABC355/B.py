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

N,M = mi()
A = li()
B = li()
a_s = set()
b_s = set()
AB = []
for a in A:
    AB.append(a)
    a_s.add(a)
for b in B:
    AB.append(b)
    b_s.add(b)

AB.sort()
now = -1
for ab in AB:
    if ab in a_s:
        if now == 1:
            print("Yes")
            exit()
        now = 1
    else:
        now = -1

print("No")
    
