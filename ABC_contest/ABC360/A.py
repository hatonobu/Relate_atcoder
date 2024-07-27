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
a = 0
b = 0
for i in range(len(S)):
    if S[i] == "R":
        a = i
        break

for i in range(len(S)):
    if S[i] == "M":
        b = i
        break

if a < b:
    print("Yes")
else:
    print("No")