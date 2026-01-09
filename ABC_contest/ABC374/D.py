import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue
import math

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

N,S,T = mi()
ABCD = lli(N)
ans_time = INF

for e1 in itertools.permutations(range(N)):
    for e2 in itertools.product(range(2),repeat=N):
        now = (0,0)
        time = 0
        for i in range(N):
            a,b,c,d = ABCD[e1[i]]
            n = e2[i]
            if n == 1:
                dist = math.sqrt((now[0]-a)**2 + (now[1]-b)**2)
                time += dist / S
                time += math.sqrt((a-c)**2 + (b-d)**2) / T
                now = (c,d)
            else:
                dist = math.sqrt((now[0]-c)**2 + (now[1]-d)**2)
                time += dist / S
                time += math.sqrt((a-c)**2 + (b-d)**2) / T
                now = (a,b)

        ans_time = min(ans_time,time)

print(ans_time)