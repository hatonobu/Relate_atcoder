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

N = ii()
A = li()
lis = A[::]
lis.sort()
ruiseki = [0]
for i in lis:
    ruiseki.append(ruiseki[-1] + i)

ans = []
for a in A:
    idx = bisect.bisect_right(lis,a)
    ans.append(ruiseki[-1] - ruiseki[idx])

print(*ans)