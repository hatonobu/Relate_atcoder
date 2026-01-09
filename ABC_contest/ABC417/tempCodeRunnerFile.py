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

N,M = mi()
A = li()
B = li()

B.sort()

now = 0
ans = []
for i in range(M):
    while(now < N):
        if A[now] >= B[i] or now >= N - 1:
            break
        else:
            ans.append(A[now])
            now += 1
            
    if A[now] < B[i]:
        ans.append(A[now])
        now += 1
    elif A[now] == B[i]:
        now += 1
    else:
        pass
    
print(*ans)