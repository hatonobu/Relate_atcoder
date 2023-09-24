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

S = input()
ans = 1

N = len(S)
for i in range(N):
    for j in range(i+1,N):
        flag = True
        for k in range((j-i+1) // 2):
            if S[i+k] != S[j-k]:
                flag = False
        if flag:
            ans = max(ans,j-i+1)

print(ans)