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

M = ii()
S1 = input()
S2 = input()
S3 = input()

ans = 10**10
for i in range(3*M):
    for j in range(3*M):
        for k in range(3*M):
            if i != j and j != k and i != k and S1[i%M] == S2[j%M] == S3[k%M]:
                ans = min(ans,max(i,j,k))

print(ans if ans < 10**10 else -1 )  
