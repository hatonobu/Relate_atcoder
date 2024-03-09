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
ans = [list("0"*N) for _ in range(N)]
ans[(N)//2][(N)//2] = "T"
now = 1

def toguro(N,times,now):
    for i in range(times,N - times):
        ans[times][i] = str(now)
        now += 1
    for j in range(times+1,N-times):
        ans[j][N-times-1] = str(now)
        now += 1
    for k in range(N-2-times,times-1,-1):
        ans[N-times-1][k] = str(now)
        now += 1
    for l in range(N-2-times,times,-1):
        ans[l][times] = str(now)
        now += 1
    return now

times = 0
for i in range(N//2):
    now = toguro(N,times,now)
    times += 1


for a in ans:
    print(" ".join(a))


    


