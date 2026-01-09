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

total = [0]*(M+1)
total_num = [0]*(M+1)

for _ in range(N):
    a,b = mi()
    total[a] += b
    total_num[a] += 1

for i in range(1,M+1):
    print(total[i]/total_num[i])