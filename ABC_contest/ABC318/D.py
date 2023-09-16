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
D = [[0]*N for _ in range(N)]
for i in range(N-1):
    d = li()
    for j in range(i+1,N):
        D[i][j] = d[j-i-1]
        D[j][i] = d[j-i-1]

def dfs(used):
    if all(used):
        return 0
    for i in range(N):
        if used[i] == False:
            used[i] = True
            num = 0
            for j in range(i+1,N):
                if used[j] == False:
                    used[j] = True
                    num = max(num,D[i][j] + dfs(used))
                    used[j] = False
            break
    return num

used = [False]*N
ans = dfs(used)
print(ans)