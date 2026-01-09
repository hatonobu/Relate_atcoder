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

S = input()

T = []
hashcheck = False
for s in S:
    T.append(s)
ans = [(k, len(list(g))) for k,g in itertools.groupby(S)]


check = []
now = -1
for s, num in ans:
    now += num
    if s == "#":
        check.append(now-num)

if len(check) > 0:
    for num in check:
        if num >= 0:
            T[num] = "o"

    if S[-1] == ".":
        T[-1] = "o"
else:
    T[0] = "o"
    
print("".join(T))