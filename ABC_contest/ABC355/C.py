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

N,T = mi()
A = li()
naname1 = set()
naname2 = set()
for i in range(N):
    naname1.add((N+1)*i+1)
    naname2.add((N-1)*i+N)

#print(naname1,naname2)
tate = [set() for _ in range(N)]
yoko = [set() for _ in range(N)]
naname = [set() for _ in range(2)]

for i in range(T):
    a = A[i]
    judge = False
    yoko[(a-1) // N].add(a)
    if len(yoko[(a-1) // N]) == N:
        judge = True   
    tate[((a-1)%N)].add(a)
    if len(tate[((a-1)%N)]) == N:
        judge = True
    if a in naname1:
        naname[0].add(a)
        if len(naname[0]) == N:
            judge = True
    if a in naname2:
        naname[1].add(a)
        if len(naname[1]) == N:
            judge = True
    
    if judge:
        print(i+1)
        exit()
    

print(-1)

