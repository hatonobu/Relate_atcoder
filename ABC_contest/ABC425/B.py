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

check = set()
for a in A:
    if a in check and a != -1:
        print("No")
        exit()
    check.add(a)

ans = []
for i in range(N):
    if A[i] == -1:
        for j in range(1,N+1):
            if j not in check:
                ans.append(j)
                check.add(j)
                break
    else:
        ans.append(A[i])

print("Yes")
print(*ans)