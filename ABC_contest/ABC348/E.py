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
    
N = ii()
AB = lli(N-1)
C = li()

G1 = [ []for _ in range(N+1)]
G2 = [ []for _ in range(N+1)]

for a,b in AB:
    G1[a].append(b)
    G2[b].append(a)

print(G1,G2)
