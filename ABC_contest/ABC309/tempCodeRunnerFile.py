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
P = li()

g = [[] for _ in range(N)]
for i,num in enumerate(P,2):
    g[num-1].append(i-1)


used = [False]*N
ans = [False]*N

def BFS(s,roop,times):
    ans[s] = True
    times += 1
    if roop < times:
        return
    
    if used[s] == False:
        used[s] = True
        for nxt in g[s]:
            ans[nxt] = True
            if used[nxt] == False:
                BFS(nxt,roop,times)              
    else:
        return
    
lis = [-1]*N
for _ in range(M):
    x,y = mi()
    lis[x-1] = max(lis[x-1],y)

for i in range(N-1,-1,-1):
    if lis[i] == -1:
        continue
    else:
        BFS(i,lis[i],0)

Ans = 0
for i in range(N):
    if ans[i] == True:
        Ans += 1

print(Ans)