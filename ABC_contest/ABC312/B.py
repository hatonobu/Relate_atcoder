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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N,M = mi()

S = [input() for _ in range(N)]

def check(x,y):
    for i in range(3):
        for j in range(3):
            if not S[y+i][x+j] == "#":
                return False
    return True

def yoko(x,y):
    for i in range(4):
        if S[y][x+i] == "#":
            return False
    return True

def tate(x,y):
    for j in range(4):
        if S[y+j][x] == "#":
            return False
    return True

for y in range(N-8):
    for x in range(M-8):
        if check(x,y) and check(x+6,y+6) and tate(x+3,y) and tate(x+5,y+5) and yoko(x,y+3) and yoko(x+5,y+5):
            print(y+1,x+1)
           
