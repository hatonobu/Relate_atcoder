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
B = li()
A.sort(reverse=True)
B.sort(reverse=True)

ans = -1
now = 0
for i in range(N-1):
    if B[i] >= A[now]:
        now += 1
    else:
        if B[i] >= A[now+1]:
            if ans != -1:
                print(-1)
                exit()
            else:
                ans = A[now]
                now += 2
        else:
            print(-1)
            exit()

if ans == -1:
    print(A[-1])
else:
    print(ans)          
    