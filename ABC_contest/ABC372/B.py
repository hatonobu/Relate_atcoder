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

M = ii()

ans = []
while(M > 0):
    i = 0
    while(True):
        if 3**i > M:
            M -= 3**(i-1)
            ans.append(i-1)
            break
        i += 1
        
print(len(ans))
print(*ans)
    