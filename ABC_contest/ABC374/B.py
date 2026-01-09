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

S = list(input())
T = list(input())

if len(S) < len(T):
    for i in range((len(T) - len(S))):
        S.append("-")
else:
    for i in range(len(S) - len(T)):
        T.append("-")

for i in range(max(len(S),len(T))):
    if S[i] != T[i]:
        print(i+1)
        exit()

print(0)