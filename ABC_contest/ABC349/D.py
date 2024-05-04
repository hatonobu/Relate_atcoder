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

L,R = mi()
ans = []


while(L < R):
    l_max = L
    for i in range(61):
        num = 2**i
        if L % num == 0:
            n = L // num
            if (num * (n+1)) > R:
                break
            l_max = max(l_max,(num * (n+1)))
    ans.append([L,l_max])
    L = l_max

print(len(ans))
for l in ans:
    print(*l)