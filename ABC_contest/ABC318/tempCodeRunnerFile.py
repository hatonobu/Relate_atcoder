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
A = li()
d1 = defaultdict(list)

ans = 0
check = set()
for i in range(N):
    num = A[i]
    if len(d1[num]):
        check.add(num)
        d1[num].append(i)
    else:
        d1[num].append(i)

check = list(check)
ans = 0
for n in check:
    l = d1[n]
    times = len(l)
    for k in range(times-1):
        ans += ((times - 1 - k) * (k+1)) * (l[k+1] - l[k] - 1)
    
print(ans)
