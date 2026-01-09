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

N,M = mi()
ABC = []
for _ in range(M):
    A,B = mi()
    ABC.append((A,B,A-B))
ABC.sort(key=lambda x: x[2], reverse=True)

ans = 0
while(ABC):
    a,b,c = ABC.pop()
    if N >= a:
        num = (N-a) // c + 1
        N -= num*c
        ans += num

print(ans)