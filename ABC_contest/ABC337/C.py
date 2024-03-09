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
lis = [-1]*N

s = -1
for i,a in enumerate(A):
    if a == -1:
        s = i
        continue
    lis[a-1] = i+1

ans = [s+1]
while(1):
    num = lis[s]
    if num == -1:
        break
    ans.append(num)
    s = num - 1
    if len(ans) == N:
        break

print(*ans)