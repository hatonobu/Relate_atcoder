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

H,W = mi()
Sy, Sx = mi()
Sy -= 1
Sx -= 1
C = [list(input()) for _ in range(H)]
X = input()

def check(x,y):
    if x < 0:
        x = 0
    elif x >= W:
        x = W-1
    
    if y < 0:
        y = 0
    elif y >= H:
        y = H-1
    
    return x,y
for s in X:
    if s == "U":
        Sy -= 1
        Sx,Sy = check(Sx,Sy)
        if C[Sy][Sx] == "#":
            Sy += 1

    elif s == "R":
        Sx += 1
        Sx,Sy = check(Sx,Sy)
        if C[Sy][Sx] == "#":
            Sx -= 1
    elif s == "L":
        Sx -= 1
        Sx,Sy = check(Sx,Sy)
        if C[Sy][Sx] == "#":
            Sx += 1
    else:
        Sy += 1
        Sx,Sy = check(Sx,Sy)
        if C[Sy][Sx] == "#":
            Sy -= 1

print(Sy+1,Sx+1)