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

Q = ii()
lis = [0]

ans = []
now = 0
for i in range(Q):
    a = li()
    if a[0] == 1:
        num,l = a
        lis.append(lis[-1] + l)
    elif a[0] == 2:
        num = a[0]
        now += 1
    else:
        num,k = a
        ans.append(lis[k+now-1] - lis[now])

print(*ans, sep="\n")
        