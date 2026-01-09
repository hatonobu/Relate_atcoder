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

T = input()
U = input()

ans = False
for i in range(len(T)- len(U)+1):
    f = True
    for j in range(len(U)):
        if T[i+j] == U[j] or T[i+j] == "?":
            pass
        else:
            f = False
    if f:
        ans = True

print("Yes" if ans else "No")