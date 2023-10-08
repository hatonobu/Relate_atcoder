import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
A = li()

lis = []
for i in range(N):
    num = min(A[i],A[(i-1)%N])
    lis.append(num)

ans = 0
check = [0]*N
c = []
for i in range(N):
    if check[(i-1)%N] >= 1:
        continue
    if lis[i] == A[(i-1)%N]:
        check[(i-1)%N] += 1
    else:
        check[i] += 1
    c.append(lis[i])

print(c)
print(*lis)
print(check)
print(ans)