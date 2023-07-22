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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,D = mi()
S = [input() for _ in range(N)]
ans = 0

check = 0
for i in range(D):
    for j in range(N):
        if S[j][i] == "x":
            ans = max(ans,check)
            check = 0
            break
        else:
            if j == N-1:
                check += 1

ans = max(ans,check)
print(ans)