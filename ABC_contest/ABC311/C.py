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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
A = li()

used = [False]*(N+3)
ans = []

def dfs(start,used):
    if used[start-1] == True:
        num = start
        while(1):
            next = A[start-1]
            ans.append(next)
            if next == num:
                print(len(ans))
                print(*ans)
                exit()
            start = next
    else:
        used[start-1] = True
        dfs(A[start-1],used)

dfs(1,used)
    