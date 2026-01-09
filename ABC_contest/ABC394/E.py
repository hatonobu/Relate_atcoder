import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
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

C = [list(input()) for _ in range(N)]

ans = [[INF]*N for _ in range(N)]

q = []
for i in range(N):
    q.append((i,i))
    ans[i][i] = 0

for i in range(N):
    for j in range(N):
        if i == j:
            pass
        elif C[i][j] != "-":
            q.append((i,j))
            ans[i][j] = 1

while q:
    x,y = q.pop(0)
    for i in range(N):
        for j in range(N):
            if (C[i][x] != "-" and C[y][j] != "-" and C[i][x] == C[y][j] and ans[i][j] == INF):
                ans[i][j] = ans[x][y] + 2
                q.append((i,j))

for i in range(N):
    ans_lis = []
    for num in ans[i]:
         ans_lis.append(-1 if num == INF else num)
    print(*ans_lis)

        
        
