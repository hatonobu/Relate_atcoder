import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

sys.setrecursionlimit(10 ** 9)
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
cost = dict()
G = [[] for _ in range(N)]
totalTreeCost = 0

for i in range(N-1):
    a,b,c = mi()
    a -= 1
    b -= 1
    cost[(a,b)] = c
    cost[(b,a)] = c
    G[a].append(b)
    G[b].append(a)
    totalTreeCost += 2*c

used = [False]*N
q = deque()
q.append((0,0))
lis = [0]*N
used[0] = True
while(q):
    now, totalCost = q.popleft()
    for next in G[now]:
        if used[next]:
            pass
        else:
            nextCost = totalCost + cost[(now,next)]
            lis[next] = nextCost
            used[next] = True
            q.append((next,nextCost))

nextIndex = -1
maxNum = -1
for i in range(N):
    if maxNum < lis[i]:
        nextIndex = i
        maxNum = lis[i]


used = [False]*N
q = deque()
q.append((nextIndex,0))
lis = [0]*N
used[nextIndex] = True
while(q):
    now, totalCost = q.popleft()
    for next in G[now]:
        if used[next]:
            pass
        else:
            nextCost = totalCost + cost[(now,next)]
            lis[next] = nextCost
            used[next] = True
            q.append((next,nextCost))

print(totalTreeCost - max(lis))