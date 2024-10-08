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
S = []
for i in range(N):
    s = input()
    s += "*"*100
    S.append(s)

ans = [""]*(100)
for i in range(N):
    checkS = S[-1-i]
    for j in range(100):
        ans[j] += checkS[j]

for a in ans:
    for k in range(len(a)-1,-1,-1):
        if a[k] != "*":
            print(a[:k+1])
            break

