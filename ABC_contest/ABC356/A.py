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

N,L,R = mi()

ans = []
for i in range(1,L):
    ans.append(i)
for j in range(R,L-1,-1):
    ans.append(j)
for k in range(R+1,N+1):
    ans.append(k)

print(*ans)