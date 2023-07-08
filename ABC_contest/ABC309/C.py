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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,K = mi()
lis = []
sum = 0
day = 0
for i in range(N):
    a,b = mi()
    sum += b
    day = max(day,a)
    lis.append((a,b))

lis.sort()

if sum <= K:
    print(1)
    exit()
for x,y in lis:
    sum -= y
    if sum <= K:
        print(x+1)
        exit()