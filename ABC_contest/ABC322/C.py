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

N,M = mi()
A = li()
ans = [0]*N

num = 0
for i in range(1,N):
    if num == M - 1:
        ans[i-1] = A[-1] - i
    else:
        while(num < M):
            if A[num] < i:
                num += 1
            else:
                break
        ans[i-1] = A[num] - i

print(*ans,sep="\n")