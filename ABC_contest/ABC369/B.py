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
ans = 0
l = -1
r = -1

for i in range(N):
    num, d = ml()
    num = int(num)
    if d == "L":
        if l == -1:
            pass
        else:
            ans += max(l,num) - min(l,num)
        l = num
    else:
        if r == -1:
            pass
        else:
            ans += max(r,num) - min(r,num)
        r = num

print(ans)
