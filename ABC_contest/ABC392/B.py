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

N,M = mi()
A = li()
A.sort()
ans = []

now = 1
for a in A:
    while(now <= N):
        if now == a:
            now += 1
            break
        else:
            ans.append(now)
            now += 1


while(now <= N):
    ans.append(now)
    now += 1
    
print(len(ans))
print(*ans)
        
