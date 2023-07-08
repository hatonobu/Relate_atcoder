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
 
N = ii()
S = [input() for _ in range(N)]
A = []
 
for i in S:
    A.append(list(i))
 
for i in range(N):
    for j in range(N):
        if i == 0:
            if j == N-1:
                A[i+1][j] = S[i][j]
            else:
                A[i][j+1] = S[i][j]
        elif i == N-1:
            if j == 0:
                A[i-1][j] = S[i][j]
            else:
                A[i][j-1] = S[i][j]
        else:
            if j == 0:
                A[i-1][j] = S[i][j]
            elif j == N-1:
                A[i+1][j] = S[i][j]
            else:
                pass
 
for i in A:
    for j in i:
        print(j,end="")
    print()