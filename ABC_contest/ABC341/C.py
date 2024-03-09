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

H,W,N = mi()
T = input()
S = [list(input()) for _ in range(H)]

ans = 0

def check(y,x):
    for s in T:
        if s == "R":
            x += 1
        elif s == "L":
            x -= 1
        elif s == "U":
            y -= 1
        elif s == "D":
            y += 1
        if 0 <= x < W and 0 <= y < H:
            if S[y][x] == "#":
                return False
        else:
            return False
    return True

for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            if check(y,x):
                ans += 1
            
print(ans)