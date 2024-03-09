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

A = li()

check = [0]*10
for a in A:
    check[a] += 1

ans = 0

total = 0
check1 = check[:]
for i in range(1,9):
    if check1[i-1] >= 1 and check1[i] >= 1 and check1[i+1] >= 1:
        n = min(check1[i-1],check1[i],check1[i+1])
        check1[i-1] -= n
        check1[i] -= n
        check1[i+1] -= n
        total += n
for i in range(10):
    if check1[i] >= 3:
        total += 2* (check1[i] // 3)

ans = max(ans,total)

total = 0
check1 = check[:]
for i in range(10):
    if check1[i] >= 3:
        n = check1[i] // 3
        total += 2*n
        check1[i] -= 3*n
for i in range(1,9):
    if check1[i-1] >= 1 and check1[i] >= 1 and check1[i+1] >= 1:
        n = min(check1[i-1],check1[i],check1[i+1])
        check1[i-1] -= n
        check1[i] -= n
        check1[i+1] -= n
        total += n

ans = max(ans,total)

print(ans)