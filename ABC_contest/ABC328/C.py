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

N,Q = mi()
S = input()
R = [0]
for i in range(N-1):
    if S[i] == S[i+1]:
        R.append(R[-1]+1)
    else:
        R.append(R[-1])

ans = []
for i in range(Q):
    l,r = mi()
    ans.append(R[r-1] - R[l-1])

print(*ans,sep="\n")
