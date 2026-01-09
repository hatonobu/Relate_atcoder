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

N,M = mi()
P = li()
check = []

d = defaultdict(deque)

for i in P:
    heapq.heappush(check,i)
    d[i].append(1)
    
ans = 0
total = 0
while(len(check) > 0):
    num = heapq.heappop(check)
    if total + num <= M:
        total += num
        ans += 1
        times = d[num].popleft() + 1
        next_num = num * times**2
        heapq.heappush(check,next_num)
        d[next_num].append(times)
    else:
        break

print(ans)