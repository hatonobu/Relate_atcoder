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
P = lli(N)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if P[i][0] >= P[j][0]:
                check = set(P[i][2:] + P[j][2:])
                if len(check) == P[j][1]:
                    if P[i][0] > P[j][0] or P[i][1] < P[j][1]:
                        print("Yes")
                        exit()

print("No")