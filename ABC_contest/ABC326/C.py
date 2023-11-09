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

N,M = mi()
A = li()
A.sort()
ans = 0
q = deque()

for a in A:
    q.append(a)
    while(1):
        if not q:
            break
        if q[-1] - q[0] + 0.01 > M:
            q.popleft()
        else:
            break

    ans = max(len(q),ans)

print(ans)