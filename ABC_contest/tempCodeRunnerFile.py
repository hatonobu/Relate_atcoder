import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

H,W = mi()
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
    num = 0
    for j in range(W):
        if S[i][j] == ".":
            num += 1
        else:
            ans += max(0,num - 1)
            num = 0

for i in range(W):
    num = 0
    for j in range(H):
        if S[j][i] == ".":
            num += 1
        else:
            ans += max(0,num - 1)
            num = 0
    ans += max(0,num - 1)

print(ans)