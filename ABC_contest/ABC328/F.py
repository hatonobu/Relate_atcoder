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

N,Q = mi()
ans = []
INF = 8 * 10**18
check = [INF] * (N+1)
for i in range(Q):
    a,b,d = mi()

    num1,num2 = check[a], check[b]
    if num1 == INF and num2 == INF:
        check[a] = d
        check[b] = 0
    elif num1 == INF and num2 != INF:
        check[a] = num2 + d
    elif num2 == INF and num1 != INF:
        check[b] = num1 - d
    else:
        pass

    num11,num22 = check[a], check[b]
    if num11 - num22 == d:
        ans.append(i+1)
    else:
        check[a] = num1
        check[b] = num2
    
print(*ans)