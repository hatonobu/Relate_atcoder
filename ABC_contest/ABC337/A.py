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
total = [0,0]

for i in range(N):
    x,y = mi()
    total[0] += x
    total[1] += y

if total[0] > total[1]:
    print("Takahashi")
elif total[0] == total[1]:
    print("Draw")
else:
    print("Aoki")