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
up = [0]*N
down = [0]*N

left = 0
right = 0
for i in range(N):
    if left < A[i]:
        left += 1
    else:
        left = A[i]
    up[i] = left

for i in range(N):
    if right < A[-i-1]:
        right += 1
    else:
        right = A[-i-1]
    down[-i-1] = right

ans = 1
for i in range(1,N-1):
    ans = max(ans,min(A[i],min(up[i-1],down[i+1])+1))

#print(up)
#print(down)
print(ans)