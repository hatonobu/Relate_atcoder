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

N = ii()
A = li()

pos = [-1]*N
for i in range(N):
    pos[A[i]-1] = i

ans = []
for j in range(N):
    if A[j] == j+1:
        continue
    ans.append([j+1,pos[j]+1])
    num = A[j]
    A[j] , A[pos[j]] = A[pos[j]], A[j] 
    pos[j], pos[num-1] = pos[num-1], pos[j]
    #print(A,pos)

print(len(ans))
for n in ans:
    print(*n)