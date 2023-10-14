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

N,T = ml()
N = int(N)
S = [input() for _ in range(N)]
T_l = len(T)
front = [0]*(T_l+1)
back = [0]*(T_l+1)

for i in range(N):
    s = S[i]
    now = 0
    for ss in s:
        if now >= T_l:
            break
        if ss == T[now]:
            now += 1
    front[now] += 1
    s = s[::-1]
    now = T_l - 1
    for ss in s:
        if now < 0:
            break
        if ss == T[now]:
            now -= 1
    back[T_l - (now + 1)] += 1

ru_front = [0]
ru_back = [back[-1]]
for f in front:
    ru_front.append(ru_front[-1] + f)
for i in range(T_l):
    ru_back.append(ru_back[-1] + back[-2-i])

ans = 0
for i in range(T_l+1):
    ans += front[i] * ru_back[i]

print(ans)