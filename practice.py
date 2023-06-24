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
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,M = mi()
AB = lli(M)
CD = lli(M)
d1 = defaultdict(list)
d2 = defaultdict(list)
 
for x,y in AB:
    d1[x-1].append(y-1)
    d1[y-1].append(x-1)
for x,y in CD:
    d2[x-1].append(y-1)
    d2[y-1].append(x-1)
 
print(d1,d2)

ans = False
if ans:
    print("Yes")
else:
    print("No")