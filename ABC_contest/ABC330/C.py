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

D = ii()
check = []
for i in range(2*10**6):
    check.append(i*i)
    if i*i > D:
        break
    
ans = 10**18
for i in range(2*10**6):
    if i*i > D:
        break
    idx = bisect.bisect_left(check,D-(i*i))
    #sprint(idx,check[idx],i*i)
    for j in range(-2,3):
        if 0 <= idx+j < len(check):
            num = abs(i*i + check[idx+j] - D)
            #print(num)
            #print(num,i*i)
            ans = min(ans,num)

print(ans)