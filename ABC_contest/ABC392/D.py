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

N = ii()
KA = lli(N)
d = defaultdict(set)
lis = [[0]*(10**5+2) for _ in range(N+1)]

for i in range(N):
    num, l = KA[i][0], KA[i][1:]
    for n in l:
        d[i].add(n)
        lis[i][n] += 1

ans = 0
for e in itertools.combinations(range(N),2):
    num = 0
    bunbo = KA[e[0]][0] * KA[e[1]][0]
    for dice in d[e[0]]:
        num += lis[e[0]][dice] * lis[e[1]][dice]
    
    ans = max(ans, num/bunbo)

print(ans)

