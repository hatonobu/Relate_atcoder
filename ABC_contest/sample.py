import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
A = lli(2*N - 1)
ans = 0

def dfs(used,B):
    global ans
    if all(used):
        ans = max(ans,B)
        return True
    a = used.index(False)
    used[a] = True
    for num in range(a+1,2*N):
        if used[num] == False:
            B_next = B ^ A[a][num-a-1]
            #print(A[a][num-a-1])
            used[num] = True
            dfs(used,B_next)
            used[num] = False
    used[a] = False
    return B

used = [False] * (2*N)
aa = dfs(used,0)
print(ans)




