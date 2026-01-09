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
server = -1
word = defaultdict(list)
check = [-1] * (N + 1)
for _ in range(Q):
    l = li_st()
    l[0] = int(l[0])
    l[1] = int(l[1])
    if l[0] == 1:
        p = l[1]
        PC[p] = PC[server][0]
    elif l[0] == 2:
        p = l[1]
        s = l[2]
        PC[p].append(s)
    else:
        p = l[1]
        PC[p] = ["".join(PC[p])]
        server = p

print(PC[server][0])