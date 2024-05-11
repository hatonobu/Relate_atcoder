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

check = [0]*11
for a in A:
    num = len(str(a))
    check[num] += 1

ans = 0
for i in range(N):
    n = A[i]
    num = len(str(n))
    check[num] -= 1
    ans += n * i
    ans %= mod
    for j in range(1,11):
        ans += n * check[j] * 10**j
        ans %= mod
    
print(ans)