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

N,L = mi()

d = li()

if L % 3 != 0:
    print(0)
else:
    lis = [0] * (L + 1)
    now = 0
    lis[0] = 1
    for i in d:
        now += i
        now %= L
        lis[now] += 1
    ans = 0
    for i in range(L // 3):
        ans += lis[i] * lis[i + L // 3] * lis[i + 2 * (L // 3)]
    print(ans)