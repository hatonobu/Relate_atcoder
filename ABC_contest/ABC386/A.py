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

N = li()
d = defaultdict(int)

for i in N:
    d[i] += 1

if len(d) != 2:
    print("No")
    exit()

lis = []
for number, sum in d.items():
    lis.append(sum)

if (lis[0] == 2 and lis[1] == 2) or (lis[0] == 3 and lis[1] == 1) or (lis[1] == 3 and lis[0] == 1):
    print("Yes")
else:
    print("No")
