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

N,X,Y = mi()
a = li()
b = li()
A = defaultdict(int)
B = defaultdict(int)

lis_a = []
lis_b = []
for i in range(N):
    A[i] = a[i]
    lis_a.append((a[i],i))
    B[i] = b[i]
    lis_b.append((b[i],i))

lis_a.sort(reverse=True)
lis_b.sort(reverse=True)

ans = INF
totalSweet = 0
totalSalty = 0
now = 0
for num,idx in lis_a:
    now += 1
    totalSweet += num
    totalSalty += B[idx]

    if totalSweet > X:
        break
    if totalSalty > Y:
        break

ans = min(ans,now)

totalSweet = 0
totalSalty = 0
now = 0
for num,idx in lis_b:
    now += 1
    totalSweet += A[idx]
    totalSalty += num

    if totalSweet > X:
        break
    if totalSalty > Y:
        break


ans = min(ans,now)

print(ans)


