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

N = ii()
S = [input() for _ in range(N)]
tate = [0]*N
yoko = [0]*N
for i in range(N):
    s = S[i]
    for j in range(N):
        if s[j] == "o":
            tate[j] += 1
            yoko[i] += 1

ans = 0
for i in range(N):
    for j in range(N):
        x = tate[j] * (tate[j]-1) // 2 #nC2
        y = yoko[i] * (yoko[i]-1) // 2 #nC2
        if S[i][j] == "o":
            ans += max(0,(tate[j]-1) * (yoko[i]-1))

print(ans)