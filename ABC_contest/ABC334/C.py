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

N,K = mi()
A = set(li())
ans = 0
lis = []
for i in range(1,N+1):
    lis.append(i)
    if not i in A:
        lis.append(i)

if K % 2 == 0:
    ans = 0
    for i in range(0,len(lis),2):
        ans += lis[i+1] - lis[i]
else:
    f_ruiseki = [0]
    b_ruiseki = [0]
    ans = INF
    for i in range(0,len(lis)-1,2):
        f_ruiseki.append(f_ruiseki[-1] + (lis[i+1] - lis[i]))
    for i in range(len(lis)-1,0,-2):
        b_ruiseki.append(b_ruiseki[-1] + (lis[i] - lis[i-1]))
    for j in range(len(f_ruiseki)):
        ans = min(ans,f_ruiseki[j] + b_ruiseki[-j-1])

print(ans)