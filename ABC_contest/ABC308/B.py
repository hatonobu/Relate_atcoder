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

N,M = mi()
C = li_st()
D = li_st()
P = li()

ans = 0
for s in C:
    for j in range(M):
        num = 0
        if s == D[j]:
            num = j+1
            break
    ans += P[num]

print(ans)

