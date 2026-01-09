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

H,W,D = mi()
S = [list(input()) for _ in range(H)]

yuka = []
for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            yuka.append((x,y))
                

ans = 0
for e in itertools.combinations(range(len(yuka)),2):
    x1,y1 = yuka[e[0]]
    x2,y2 = yuka[e[1]]
    
    set_list = set()
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                if (abs(i-y1) + abs(j-x1)) <= D or (abs(i-y2) + abs(j-x2)) <= D:
                    set_list.add((i,j))
    ans = max(ans,len(set_list))

print(ans)
