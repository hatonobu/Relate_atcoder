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
lis = []
for i in range(N):
    lis.append([0.01*(1-(i+1)),i+1])

for i in range(N):
    for s in S[i]:
        if s == "o":
            lis[i][0] += 1

lis.sort(reverse=True)
ans = []
for n in lis:
    ans.append(n[1])

print(*ans)