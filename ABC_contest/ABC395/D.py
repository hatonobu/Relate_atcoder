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

N,Q = mi()
lis_place = [0]*(N+1)
lis_num = [0]*(N+1)
d = defaultdict(int)
for i in range(N+1):
    lis_place[i] = i
    lis_num[i] = i
    d[i] = i

ans = []
for i in range(Q):
    op1 = li()
    if op1[0] == 1:
        a,b = op1[1],op1[2]
        lis_place[a] = d[b]
        
    elif op1[0] == 2:
        a,b = op1[1],op1[2]
        d[a],d[b] = d[b],d[a]
        lis_num[d[a]],lis_num[d[b]] = lis_num[d[b]],lis_num[d[a]]
           
    else:
        a = op1[1]
        ans.append(lis_num[lis_place[a]])

print(*ans, sep="\n")