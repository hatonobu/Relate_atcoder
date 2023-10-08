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

N,M = mi()
A = li()
S = [input() for _ in range(N)]
score = [0]*N
for i in range(N):
    score[i] += i+1
    for j in range(M):
        if S[i][j] == "o":
            score[i] += A[j]

check = []
for i in range(M):
    check.append([i,A[i]])

check.sort(key=lambda x:x[1],reverse=True)

m = max(score)
for i in range(N):
    ans = 0
    if score[i] == m:
        print(0)
        continue
    else:
        for j,s in check:
            if score[i] > m:
                break
            if S[i][j] == "x":
                score[i] += s
                ans += 1
        print(ans)