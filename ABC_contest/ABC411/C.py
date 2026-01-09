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

N,Q = mi()
A = li()

check = [0] * (N + 2)
ans = 0

for a in A:
    if check[a] == 0:
        check[a] = 1
        if check[a - 1] == 0 and check[a + 1] == 0:
            ans += 1
        elif check[a - 1] == 1 and check[a + 1] == 1:
            ans -= 1
    elif check[a] == 1:
        check[a] = 0
        if check[a - 1] == 0 and check[a + 1] == 0:
            ans -= 1
        elif check[a - 1] == 1 and check[a + 1] == 1:
            ans += 1
    print(ans)
