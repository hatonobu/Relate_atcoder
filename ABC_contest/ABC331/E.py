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

N,M,L = mi()
a = li()
b = li()
cd = set()
for i in range(L):
    c,d = mi()
    cd.add((c,d))

A = []
for i in range(N):
    A.append((a[i],i+1))
B = []
for j in range(M):
    B.append((b[j],j+1))

A.sort(reverse=True)
B.sort(reverse=True)

ans = -1
for a,num1 in A:
    for b,num2 in B:
        if (num1,num2) in cd:
            continue
        else:
            ans = max(ans,a+b)
            break

print(ans)


