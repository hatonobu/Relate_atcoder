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
A = li()

ans = 0
for i in range(N):
    check = -1
    for j in range(2*N):
        if A[j] == i+1:
            if check != -1:
                if j - check == 2:
                    ans += 1
                    break
            else:
                check = j

print(ans)
