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
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
    
N = ii()
check = []

for i in range(N):
    a,b = mi()
    num = a / (a+b)
    bisect.insort_left(check,(num,i+1))

ans = []
for x,y in check:
    ans.append(y)

print(*ans)