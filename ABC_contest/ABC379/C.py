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

N,M = mi()
d = defaultdict(int)
X = li()
A = li()
for i in range(M):
    d[X[i]] = A[i]

d= sorted(d.items(), key=lambda x:x[0])

now = 1
ans = 0

for key, value in d:
    if now < key:
        print(-1)
        exit()
    elif now == key:
        now += value
        ans += ((value-1) * value) // 2
    else:
        ans += value * (now - key) + ((value-1) * (value)) // 2
        now += value

if now == N+1:
    print(ans)
else:
    print(-1)