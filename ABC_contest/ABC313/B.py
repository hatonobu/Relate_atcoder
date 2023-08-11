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
 
N,M = mi()
 
d = defaultdict(list)
 
for _ in range(M):
    a,b = mi()
    d[a].append(b)
 
def dfs(ans,num):
    used[num] = True
    lis = d[num]
    for n in lis:
        if used[n] == False:
            dfs(ans,n)
 
for i in range(1,N+1):
    times = 0
    used = [False]*(N+3)
    dfs(i,i)
    for j in range(N+1):
        if used[j] == True:
            times += 1
    if times == N:
        print(i)
        exit()
 
print(-1)    
 

