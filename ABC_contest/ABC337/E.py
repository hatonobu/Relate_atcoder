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
M = 0
K = N
f = False
while(K > 1):
    if K % 2 == 1:
        f = True
    K //= 2
    M += 1

if f:
    M += 1

print(M,flush=True)
check = [[] for _ in range(M)]

for i in range(1,N):
    num = i
    times = 0
    while num:
        n = num % 2
        num //= 2
        if n == 1:
            check[times].append(i)
        times += 1

for c in check:
    print(len(c),*c,flush=True)

S = input()
check_lis = []
for i,s in enumerate(S):
    if s == "1":
        check_lis.append(i)

if len(check_lis) == 0:
     print(N)
else:
    ans = 0
    for c in check_lis:
        ans += 2**c
    print(ans)

        