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

S = input()
d = defaultdict(int)
lis = [0]*110

for s in S:
    n = (ord(s) - ord("a"))
    if d.get(n,0) != 0:
        lis[d[n]] -= 1
    d[n] += 1
    lis[d[n]] += 1

for i in range(110):
    if lis[i] == 0 or lis[i] == 2:
        continue
    else:
        print("No")
        exit()

print("Yes") 