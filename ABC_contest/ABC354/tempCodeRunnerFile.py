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
lis = []
for i in range(N):
    a,c = mi()
    lis.append((a,c,i))

max_c = INF
lis.sort(reverse=True)
ans = []

for a,b,c in lis:
    if b > max_c:
        pass
    else:
        ans.append(c+1)
        max_c = min(max_c,c)

ans.sort()
print(len(ans))
print(*ans)