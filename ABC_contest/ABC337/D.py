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

H,W,K = mi()
S = [input() for _ in range(H)]

ans = INF
total_min = INF
for y in range(H):
    total = 0
    q = deque()
    for x in range(W):
        if S[y][x] == "x":
            q.clear()
            total = 0
        else:
            q.append(S[y][x])
            if S[y][x] == ".":
                total += 1
            if len(q) > K:
                s = q.popleft()
                if s == ".":
                    total -= 1
            if len(q) == K:
                total_min = min(total_min,total)

ans = min(total_min,ans)

total_min = INF
for x in range(W):
    total = 0
    q = deque()
    for y in range(H):
        if S[y][x] == "x":
            q.clear()
            total = 0
        else:
            q.append(S[y][x])
            if S[y][x] == ".":
                total += 1
            if len(q) > K:
                s = q.popleft()
                if s == ".":
                    total -= 1
            if len(q) >= K:
                total_min = min(total_min,total)

ans = min(total_min,ans)
print(ans if ans != INF else -1)