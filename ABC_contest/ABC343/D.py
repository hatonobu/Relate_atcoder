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

d = defaultdict(int)
N,T = mi()
lis = [0]*(N+1)
d[0] = N

ans = []
for i in range(T):
    a,b= mi()
    d[lis[a]] -= 1
    if d[lis[a]] == 0:
        d.pop(lis[a])
    lis[a] += b
    d[lis[a]] += 1
    ans.append(len(d))
    

print(*ans,sep="\n")