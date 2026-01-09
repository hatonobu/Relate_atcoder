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

H,W,Y,X = mi()
S = [input() for _ in range(H)]
T = input()

X -= 1
Y -= 1
ans = set()

for t in T:
    if t == "U":
        if S[Y-1][X] != "#":
            Y -= 1
    elif t == "L":
        if S[Y][X-1] != "#":
            X -= 1
    elif t == "D":
        if S[Y+1][X] != "#":
            Y += 1
    else:
        if S[Y][X+1] != "#":
            X += 1
    
    if S[Y][X] == "@":
        ans.add((X,Y))

print(Y+1,X+1,len(ans))