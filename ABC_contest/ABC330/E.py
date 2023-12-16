import sys
from collections import deque,defaultdict
from sortedcontainers import SortedSet,SortedList,SortedDict
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
A = li()
check = SortedSet()
mex_check = [0]*(N+3)

for a in A:
    if a <= N:
        mex_check[a] += 1

ans = 0
for i in range(N+2):
    if mex_check[i] >= 1:
        ans += 1
    else:
        break

for i in range(N+2):
    if mex_check[i] == 0:
        check.add(i)

ans_lis = []

for i in range(Q):
    i,x = mi()
    i -= 1
    num = A[i]
    A[i] = x
    if num <= N+1:
        mex_check[num] -= 1
        if mex_check[num] == 0:
            check.add(num)

    if x <= N+1:
        if mex_check[x] == 0:
            check.discard(x)
        mex_check[x] += 1
    
    ans = check[0]
    ans_lis.append(ans)

print(*ans_lis,sep="\n")
check.bi