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
UDLR = lli(N)

G1 = [[0]*2005 for _ in range(2005)]
G2 = [[0]*2005 for _ in range(2005)]

for i in range(N):
    u,d,l,r = UDLR[i] #左上(l,u), 右下(r,d), 右上(r,u), 左下(l.d),
    #imos二次元
    G1[u][l] += 1
    G1[d+1][r+1] += 1
    G1[d+1][l] -= 1
    G1[u][r+1] -= 1
    
    G2[u][l] += i+1
    G2[d+1][r+1] += i+1
    G2[d+1][l] -= i+1
    G2[u][r+1] -= i+1


# print(G1[:5][:5])
#imos累積和計算
for y in range(2002):
    for x in range(2002):
        G1[y][x+1] += G1[y][x]
        G2[y][x+1] += G2[y][x]

for y in range(2002):
    for x in range(2002):
        G1[y+1][x] += G1[y][x]
        G2[y+1][x] += G2[y][x]

ans = [0]*(N+1)

base_ans = 0
for y in range(1,2001):
    for x in range(1,2001):
        if G1[y][x] == 0:
            base_ans += 1
        elif G1[y][x] == 1:
            ans[G2[y][x]] += 1

for i in range(1,N+1):
    print(base_ans+ans[i])
            