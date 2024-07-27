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
H = li()

check_point = [(0,10**9+5)]
ans = [0]*(N+1)
ans[0] = 1

for i in range(N):
    y = H[i]
    while(1):
        p_x, p_y = check_point.pop()
        if p_y < y:
            pass
        else:
            ans[i+1] = (ans[p_x] - 1) +  y*(i - p_x) + (y+1)
            #print(ans[p_x] +  y*(i+1 - p_x) + 1, p_x)
            check_point.append((p_x,p_y))
            break
    check_point.append((i+1,y))

print(*ans[1:])