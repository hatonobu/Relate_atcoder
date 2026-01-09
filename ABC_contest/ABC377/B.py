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

S = [input() for _ in range(8)]

def check(x,y):
    flag = True
    for i in range(8):
        if S[i][x] == "#":
            flag = False
    for j in range(8):
        if S[y][j] == "#":
            flag = False
    
    return flag

ans = 0
for i in range(8):
    for j in range(8):
        if S[i][j] == ".":
            if (check(j,i)):
                ans += 1

print(ans)            